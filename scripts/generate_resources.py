"""
Generates nomba/resources/*.py (sync + async) for every endpoint in the
official Nomba OpenAPI spec. Run once at dev time; output is committed.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

TAG_TO_MODULE = {
    "Accounts": "accounts",
    "Virtual Accounts": "virtual_accounts",
    "Online Checkout": "checkout",
    "Charge": "charge",
    "Transfers": "transfers",
    "Terminals": "terminals",
    "Transactions": "transactions",
    "Airtime and Data Vending": "airtime_data",
    "CableTV Subscription": "cabletv",
    "Electricity Vending": "electricity",
}
TAG_TO_CLASS = {
    "Accounts": "Accounts",
    "Virtual Accounts": "VirtualAccounts",
    "Online Checkout": "Checkout",
    "Charge": "Charge",
    "Transfers": "Transfers",
    "Terminals": "Terminals",
    "Transactions": "Transactions",
    "Airtime and Data Vending": "AirtimeData",
    "CableTV Subscription": "CableTv",
    "Electricity Vending": "Electricity",
}

PY_KEYWORDS = {"in", "type", "from", "import", "class", "return", "global", "is"}


def snake(name: str) -> str:
    # split into alnum tokens first (operationIds are often full phrases
    # like "CableTv lookup" or "Obtain access token")
    tokens = re.findall(r"[A-Za-z0-9]+", name)
    out_tokens = []
    for tok in tokens:
        # split camelCase / acronym boundaries within a single token
        tok = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", tok)
        tok = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", tok)
        out_tokens.extend(p for p in tok.split("_") if p)
    return "_".join(out_tokens).lower()


def resolve_schema(spec, schema):
    if not schema:
        return None
    if "$ref" in schema:
        ref_name = schema["$ref"].split("/")[-1]
        return spec["components"]["schemas"].get(ref_name)
    return schema


def safe_param_name(name: str) -> str:
    s = snake(name)
    if s in PY_KEYWORDS:
        s += "_"
    return s


def build_operation(spec, path, verb, op):
    tag = op.get("tags", [None])[0]
    module = TAG_TO_MODULE.get(tag)
    if module is None:
        return None

    op_id = op.get("operationId") or op.get("summary") or f"{verb}_{path}"
    method_name = snake(op_id)

    path_params = []
    query_params = []
    for p in op.get("parameters", []):
        if p["name"].lower() == "accountid" and p["in"] == "header":
            continue  # handled automatically by the client
        entry = {
            "name": p["name"],
            "py_name": safe_param_name(p["name"]),
            "required": p.get("required", False),
            "description": p.get("description", ""),
        }
        if p["in"] == "path":
            path_params.append(entry)
        elif p["in"] == "query":
            query_params.append(entry)

    body_required: list[str] = []
    body_optional: list[str] = []
    body_descriptions: dict[str, str] = {}
    request_body = op.get("requestBody")
    if request_body:
        schema = resolve_schema(
            spec, request_body.get("content", {}).get("application/json", {}).get("schema")
        )
        if schema and schema.get("type") == "object":
            props = schema.get("properties", {})
            required = set(schema.get("required", []))
            for prop_name, prop_schema in props.items():
                body_descriptions[prop_name] = prop_schema.get("description", "")
                if prop_name in required:
                    body_required.append(prop_name)
                else:
                    body_optional.append(prop_name)

    model = build_response_model(spec, op_id, path, verb, op)

    return {
        "module": module,
        "class_tag": TAG_TO_CLASS[tag],
        "method_name": method_name,
        "summary": op.get("summary", ""),
        "description": (op.get("description", "") or "").strip(),
        "verb": verb,
        "path": path,
        "path_params": path_params,
        "query_params": query_params,
        "body_required": body_required,
        "body_optional": body_optional,
        "body_descriptions": body_descriptions,
        "has_body": bool(request_body),
        "model_class": model[0] if model else None,
        "model_code": model[1] if model else None,
    }


def py_path_expr(path, path_params):
    expr = path
    for p in path_params:
        expr = expr.replace("{" + p["name"] + "}", "{" + p["py_name"] + "}")
    return expr


def render_signature(op, is_async: bool) -> str:
    parts = ["self"]
    for p in op["path_params"]:
        parts.append(f"{p['py_name']}: str")
    for name in op["body_required"]:
        parts.append(f"{safe_param_name(name)}")
    kw_only = []
    for p in op["query_params"]:
        default = "" if p["required"] else " = None"
        kw_only.append(f"{p['py_name']}: str{' | None' if not p['required'] else ''}{default}")
    for name in op["body_optional"]:
        kw_only.append(f"{safe_param_name(name)}: object | None = None")
    if kw_only:
        parts.append("*")
        parts.extend(kw_only)
    parts.append("**extra: object")
    return ", ".join(parts)


def render_method(op, is_async: bool) -> str:
    lines = []
    sig = render_signature(op, is_async)
    async_kw = "async " if is_async else ""
    await_kw = "await " if is_async else ""
    return_type = f"_models.{op['model_class']}" if op["model_class"] else "dict[str, Any]"
    lines.append(f"    {async_kw}def {op['method_name']}({sig}) -> {return_type}:")

    doc_lines = []
    if op["summary"]:
        doc_lines.append(op["summary"])
    if op["description"] and op["description"] != op["summary"]:
        doc_lines.append("")
        doc_lines.append(op["description"])
    if op["body_required"] or op["body_optional"]:
        doc_lines.append("")
        doc_lines.append("Body fields:")
        for name in op["body_required"]:
            desc = op["body_descriptions"].get(name, "")
            doc_lines.append(f"    {name} (required): {desc}")
        for name in op["body_optional"]:
            desc = op["body_descriptions"].get(name, "")
            doc_lines.append(f"    {name}: {desc}")
    if doc_lines:
        lines.append('        """')
        for line in doc_lines:
            lines.append(f"        {line}" if line else "")
        lines.append('        """')

    # build path
    path_expr = py_path_expr(op["path"], op["path_params"])
    lines.append(f'        path = f"{path_expr}"')

    if op["query_params"]:
        lines.append("        params: dict[str, object] = {}")
        for p in op["query_params"]:
            lines.append(f"        if {p['py_name']} is not None:")
            lines.append(f'            params["{p["name"]}"] = {p["py_name"]}')
    else:
        lines.append("        params = None")

    if op["has_body"] and op["verb"] in ("post", "put", "delete", "patch"):
        lines.append("        body: dict[str, object] = {}")
        for name in op["body_required"]:
            lines.append(f'        body["{name}"] = {safe_param_name(name)}')
        for name in op["body_optional"]:
            lines.append(f"        if {safe_param_name(name)} is not None:")
            lines.append(f'            body["{name}"] = {safe_param_name(name)}')
        lines.append("        body.update(extra)")
        lines.append(f'        validate_body("{op["verb"]}", "{op["path"]}", body)')
        lines.append(
            f'        return {await_kw}self._client.{op["verb"]}(path, json=body, params=params)  # type: ignore[return-value]'
        )
    else:
        lines.append(
            f'        return {await_kw}self._client.{op["verb"]}(path, params=params)  # type: ignore[return-value]'
        )

    return "\n".join(lines)


def py_type_for_schema(spec, schema, depth=0):
    """Map an OpenAPI schema to a Python type expression string. Only goes
    one level deep into nested objects/arrays; deeper nesting falls back to
    dict[str, Any] / list[Any] to keep generated models bounded."""
    schema = resolve_schema(spec, schema) or {}
    t = schema.get("type")
    if t == "string":
        return "str"
    if t == "integer":
        return "int"
    if t == "number":
        return "float"
    if t == "boolean":
        return "bool"
    if t == "array":
        if depth == 0:
            items = schema.get("items")
            return f"list[{py_type_for_schema(spec, items, depth + 1)}]"
        return "list[Any]"
    if t == "object" or "properties" in schema:
        if depth == 0 and schema.get("properties"):
            return "dict[str, Any]"
        return "dict[str, Any]"
    return "Any"


import keyword


def is_valid_field_name(name: str) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name)


def build_response_model(spec, op_id, path, verb, op):
    """Build a (class_name, code) pair for a TypedDict modeling this
    operation's 200 response, or None if there's nothing useful to model().
    Field names match the actual JSON keys verbatim (camelCase) since that's
    what callers index into -- snake_casing them would make the type hints
    describe a shape that doesn't match the real dict."""
    resp = op.get("responses", {}).get("200", {})
    schema = resp.get("content", {}).get("application/json", {}).get("schema")
    schema = resolve_schema(spec, schema)
    if not schema or schema.get("type") != "object":
        return None
    props = schema.get("properties", {})
    if not props:
        return None

    base_name = "".join(w.capitalize() for w in snake(op_id).split("_"))
    class_name = f"{base_name}Response"

    def field_lines(properties):
        out = []
        for name, sub in properties.items():
            if not is_valid_field_name(name):
                continue  # skip fields that can't be valid Python identifiers
            out.append(f"    {name}: {py_type_for_schema(spec, sub)}")
        return out

    if set(props.keys()) >= {"code", "description"} and "data" in props:
        data_schema = resolve_schema(spec, props["data"])
        data_props = (data_schema or {}).get("properties", {})
        if data_props:
            data_class = f"{base_name}Data"
            data_lines = [f"class {data_class}(TypedDict, total=False):"] + field_lines(data_props)
            data_block = "\n".join(data_lines)
            lines = [data_block, "", f"class {class_name}(TypedDict, total=False):"]
            lines.append("    code: str")
            lines.append("    description: str")
            lines.append(f"    data: {data_class}")
        else:
            lines = [f"class {class_name}(TypedDict, total=False):"]
            lines.append("    code: str")
            lines.append("    description: str")
            lines.append("    data: dict[str, Any]")
    else:
        lines = [f"class {class_name}(TypedDict, total=False):"] + field_lines(props)
        if len(lines) == 1:
            return None

    return class_name, "\n".join(lines)


def render_module(module_name, class_tag, ops, models_module_name):
    header = (
        "# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;\n"
        "# regenerate via scripts/generate_resources.py instead.\n"
        "from __future__ import annotations\n\n"
        "from typing import Any\n\n"
        "from ..http import AsyncNombaClient, NombaClient\n"
        "from ..validation import validate_body\n"
        f"from .. import {models_module_name} as _models\n\n\n"
    )

    sync_lines = [f"class {class_tag}:"]
    sync_doc = f'    """Sync resource methods for the {class_tag} group."""\n'
    sync_lines.append(sync_doc)
    sync_lines.append("    def __init__(self, client: NombaClient) -> None:")
    sync_lines.append("        self._client = client\n")
    for op in ops:
        sync_lines.append(render_method(op, is_async=False))
        sync_lines.append("")

    async_lines = [f"class Async{class_tag}:"]
    async_doc = f'    """Async resource methods for the {class_tag} group."""\n'
    async_lines.append(async_doc)
    async_lines.append("    def __init__(self, client: AsyncNombaClient) -> None:")
    async_lines.append("        self._client = client\n")
    for op in ops:
        async_lines.append(render_method(op, is_async=True))
        async_lines.append("")

    return header + "\n".join(sync_lines) + "\n\n\n" + "\n".join(async_lines) + "\n"


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR
SPEC_PATH = REPO_ROOT / "nomba_openapi.json"
if not SPEC_PATH.exists():
    SPEC_PATH = REPO_ROOT / "src" / "nomba" / "data" / "nomba_openapi.json"
OUT_DIR = REPO_ROOT / "src" / "nomba" / "resources"
MODELS_PATH = REPO_ROOT / "src" / "nomba" / "models.py"


def main():
    spec = json.loads(SPEC_PATH.read_text())
    by_module: dict[str, list] = defaultdict(list)
    class_by_module: dict[str, str] = {}
    all_model_code: list[str] = []
    seen_model_classes: set[str] = set()

    for path, methods in spec["paths"].items():
        for verb, op in methods.items():
            if verb not in ("get", "post", "put", "delete", "patch"):
                continue
            built = build_operation(spec, path, verb, op)
            if built is None:
                continue
            by_module[built["module"]].append(built)
            class_by_module[built["module"]] = built["class_tag"]
            if built["model_class"] and built["model_class"] not in seen_model_classes:
                seen_model_classes.add(built["model_class"])
                all_model_code.append(built["model_code"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    models_header = (
        "# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;\n"
        "# regenerate via scripts/generate_resources.py instead.\n"
        "#\n"
        "# These TypedDicts describe the shape of each endpoint's response for\n"
        "# editor autocomplete / type checking. They cost nothing at runtime --\n"
        "# methods still return plain dicts; TypedDict is purely a type hint.\n"
        "from __future__ import annotations\n\n"
        "from typing import Any, TypedDict\n\n\n"
    )
    MODELS_PATH.write_text(models_header + "\n\n".join(all_model_code) + "\n")
    print(f"wrote models.py ({len(all_model_code)} response models)")

    module_names = []
    for module_name, ops in by_module.items():
        code = render_module(module_name, class_by_module[module_name], ops, "models")
        (OUT_DIR / f"{module_name}.py").write_text(code)
        module_names.append((module_name, class_by_module[module_name]))
        print(f"wrote {module_name}.py ({len(ops)} ops)")

    # __init__.py
    init_lines = []
    all_exports = []
    for module_name, class_tag in sorted(module_names):
        init_lines.append(f"from .{module_name} import Async{class_tag}, {class_tag}")
        all_exports.append(class_tag)
        all_exports.append(f"Async{class_tag}")
    init_code = "\n".join(init_lines) + "\n\n__all__ = [\n"
    for name in sorted(all_exports):
        init_code += f'    "{name}",\n'
    init_code += "]\n"
    (OUT_DIR / "__init__.py").write_text(init_code)
    print("wrote __init__.py")
    print(sorted(module_names))


if __name__ == "__main__":
    main()
