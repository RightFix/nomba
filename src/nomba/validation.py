"""
Lightweight, dependency-free validation of request bodies against Nomba's
own OpenAPI spec — specifically nested required fields that a flat method
signature can't enforce (e.g. `order={...}` in checkout order creation).

This only checks presence of required keys recursively (and a coarse
type check for "object"/"array"), not full JSON-Schema validation. It's a
local fast-fail before any network call, not a replacement for Nomba's own
server-side validation.
"""
from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources
from typing import Any

from .exceptions import NombaValidationError


@lru_cache(maxsize=1)
def _load_spec() -> dict[str, Any]:
    with resources.files("nomba.data").joinpath("nomba_openapi.json").open(
        "r", encoding="utf-8"
    ) as f:
        return json.load(f)


def _resolve(spec: dict[str, Any], schema: Any) -> Any:
    if not isinstance(schema, dict):
        return schema
    if "$ref" in schema:
        name = schema["$ref"].split("/")[-1]
        return spec["components"]["schemas"].get(name, {})
    return schema


@lru_cache(maxsize=None)
def _request_schema_key(verb: str, path_template: str) -> Any:
    spec = _load_spec()
    op = spec.get("paths", {}).get(path_template, {}).get(verb.lower())
    if not op:
        return None
    rb = op.get("requestBody")
    if not rb:
        return None
    schema = rb.get("content", {}).get("application/json", {}).get("schema")
    return _resolve(spec, schema)


def _check(spec: dict[str, Any], schema: Any, value: Any, path: str, missing: list[str]) -> None:
    schema = _resolve(spec, schema)
    if not isinstance(schema, dict):
        return
    schema_type = schema.get("type")

    if schema_type == "object" or "properties" in schema:
        if not isinstance(value, dict):
            if value is not None:
                missing.append(f"{path} (expected an object)")
            return
        for required_name in schema.get("required", []):
            if required_name not in value or value[required_name] is None:
                missing.append(f"{path}.{required_name}" if path else required_name)
        props = schema.get("properties", {})
        for key, sub_value in value.items():
            if key in props:
                _check(spec, props[key], sub_value, f"{path}.{key}" if path else key, missing)

    elif schema_type == "array":
        if not isinstance(value, list):
            return
        items_schema = schema.get("items")
        if items_schema:
            for i, item in enumerate(value):
                _check(spec, items_schema, item, f"{path}[{i}]", missing)


def validate_body(verb: str, path_template: str, body: dict[str, Any]) -> None:
    """
    Validate `body` against the requestBody schema for `verb`/`path_template`
    in Nomba's OpenAPI spec, recursively checking required fields on nested
    objects/arrays. Raises NombaValidationError listing every missing field
    if any are absent. No-ops if the spec has no requestBody for this
    operation, or no nested object/array fields to check.
    """
    schema = _request_schema_key(verb, path_template)
    if schema is None:
        return
    spec = _load_spec()
    missing: list[str] = []
    _check(spec, schema, body, "", missing)
    if missing:
        raise NombaValidationError(
            f"Missing required field(s) in request body: {', '.join(missing)}",
            missing=missing,
        )
