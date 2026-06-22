# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations


from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class Terminals:
    """Sync resource methods for the Terminals group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def assign_a_terminal_to_an_account(self, sub_account_id: str, serial_number, *, terminal_label: object | None = None, **extra: object) -> _models.AssignATerminalToAnAccountResponse:
        """
        Assign a terminal to a sub account

        You can use this endpoint to assign a terminal to an sub account.

        Body fields:
            serialNumber (required): Serial number
            terminalLabel: Terminal label
        """
        path = f"/v1/terminals/assign/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["serialNumber"] = serial_number
        if terminal_label is not None:
            body["terminalLabel"] = terminal_label
        body.update(extra)
        validate_body("post", "/v1/terminals/assign/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def assign_a_terminal_to_the_parent_account(self, serial_number, *, terminal_label: object | None = None, **extra: object) -> _models.AssignATerminalToTheParentAccountResponse:
        """
        Assign a terminal to the parent account

        You can use this endpoint to assign a terminal to the parent account.

        Body fields:
            serialNumber (required): Serial number
            terminalLabel: Terminal label
        """
        path = "/v1/terminals/assign"
        params = None
        body: dict[str, object] = {}
        body["serialNumber"] = serial_number
        if terminal_label is not None:
            body["terminalLabel"] = terminal_label
        body.update(extra)
        validate_body("post", "/v1/terminals/assign", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def un_assign_terminal_from_an_account(self, sub_account_id: str, serial_number, *, terminal_label: object | None = None, **extra: object) -> _models.UnAssignTerminalFromAnAccountResponse:
        """
        Un-assign terminal from a sub account

        You can use this endpoint to un-assign a terminal from a sub account.

        Body fields:
            serialNumber (required): Serial number
            terminalLabel: Terminal label
        """
        path = f"/v1/terminals/unassign/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["serialNumber"] = serial_number
        if terminal_label is not None:
            body["terminalLabel"] = terminal_label
        body.update(extra)
        validate_body("post", "/v1/terminals/unassign/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def un_assign_a_terminal_from_the_parent_account(self, serial_number, *, terminal_label: object | None = None, **extra: object) -> _models.UnAssignATerminalFromTheParentAccountResponse:
        """
        Un-assign a terminal from the parent account

        You can use this endpoint to un-assign a terminal from the parent account.

        Body fields:
            serialNumber (required): Serial number
            terminalLabel: Terminal label
        """
        path = "/v1/terminals/unassign"
        params = None
        body: dict[str, object] = {}
        body["serialNumber"] = serial_number
        if terminal_label is not None:
            body["terminalLabel"] = terminal_label
        body.update(extra)
        validate_body("post", "/v1/terminals/unassign", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]



class AsyncTerminals:
    """Async resource methods for the Terminals group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def assign_a_terminal_to_an_account(self, sub_account_id: str, serial_number, *, terminal_label: object | None = None, **extra: object) -> _models.AssignATerminalToAnAccountResponse:
        """
        Assign a terminal to a sub account

        You can use this endpoint to assign a terminal to an sub account.

        Body fields:
            serialNumber (required): Serial number
            terminalLabel: Terminal label
        """
        path = f"/v1/terminals/assign/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["serialNumber"] = serial_number
        if terminal_label is not None:
            body["terminalLabel"] = terminal_label
        body.update(extra)
        validate_body("post", "/v1/terminals/assign/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def assign_a_terminal_to_the_parent_account(self, serial_number, *, terminal_label: object | None = None, **extra: object) -> _models.AssignATerminalToTheParentAccountResponse:
        """
        Assign a terminal to the parent account

        You can use this endpoint to assign a terminal to the parent account.

        Body fields:
            serialNumber (required): Serial number
            terminalLabel: Terminal label
        """
        path = "/v1/terminals/assign"
        params = None
        body: dict[str, object] = {}
        body["serialNumber"] = serial_number
        if terminal_label is not None:
            body["terminalLabel"] = terminal_label
        body.update(extra)
        validate_body("post", "/v1/terminals/assign", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def un_assign_terminal_from_an_account(self, sub_account_id: str, serial_number, *, terminal_label: object | None = None, **extra: object) -> _models.UnAssignTerminalFromAnAccountResponse:
        """
        Un-assign terminal from a sub account

        You can use this endpoint to un-assign a terminal from a sub account.

        Body fields:
            serialNumber (required): Serial number
            terminalLabel: Terminal label
        """
        path = f"/v1/terminals/unassign/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["serialNumber"] = serial_number
        if terminal_label is not None:
            body["terminalLabel"] = terminal_label
        body.update(extra)
        validate_body("post", "/v1/terminals/unassign/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def un_assign_a_terminal_from_the_parent_account(self, serial_number, *, terminal_label: object | None = None, **extra: object) -> _models.UnAssignATerminalFromTheParentAccountResponse:
        """
        Un-assign a terminal from the parent account

        You can use this endpoint to un-assign a terminal from the parent account.

        Body fields:
            serialNumber (required): Serial number
            terminalLabel: Terminal label
        """
        path = "/v1/terminals/unassign"
        params = None
        body: dict[str, object] = {}
        body["serialNumber"] = serial_number
        if terminal_label is not None:
            body["terminalLabel"] = terminal_label
        body.update(extra)
        validate_body("post", "/v1/terminals/unassign", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

