# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations

from typing import Any

from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class DirectDebits:
    """Sync resource methods for the DirectDebits group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def get_mandates_by_filters(
        self,
        *,
        page: str,
        page_size: str,
        from_: str | None = None,
        to: str | None = None,
        status: str | None = None,
        **extra: object,
    ) -> _models.GetMandatesByFiltersResponse:
        """
        Get mandates by filters
        """
        path = f"/v1/direct-debits/mandates"
        params: dict[str, object] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if from_ is not None:
            params["from"] = from_
        if to is not None:
            params["to"] = to
        if status is not None:
            params["status"] = status
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def update_mandate_status(
        self, mandate_id, status, **extra: object
    ) -> _models.UpdateMandateStatusResponse:
        """
        Update mandate status

        Updates the status of a direct debit mandate (e.g., SUSPEND, ACTIVE).

        Body fields:
            mandateId (required): Unique identifier of the mandate
            status (required): New status of the mandate
        """
        path = f"/v1/direct-debits/update-status"
        params = None
        body: dict[str, object] = {}
        body["mandateId"] = mandate_id
        body["status"] = status
        body.update(extra)
        validate_body("put", "/v1/direct-debits/update-status", body)
        return self._client.put(path, json=body, params=params)  # type: ignore[return-value]

    def debit_a_mandate(
        self, mandate_id, amount, **extra: object
    ) -> _models.DebitAMandateResponse:
        """
        Debit a mandate

        Debits a customer's account using an active mandate.

        Body fields:
            mandateId (required): Unique identifier of the mandate to debit
            amount (required): Amount to be debited
        """
        path = f"/v1/direct-debits/debit-mandate"
        params = None
        body: dict[str, object] = {}
        body["mandateId"] = mandate_id
        body["amount"] = amount
        body.update(extra)
        validate_body("post", "/v1/direct-debits/debit-mandate", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def get_mandate_status(
        self, *, mandate_id: str, **extra: object
    ) -> _models.GetMandateStatusResponse:
        """
        Get Mandate Status

        Fetches the status of a specific mandate by mandateId.
        """
        path = f"/v1/direct-debits/status?mandateId={mandate_id}"
        params: dict[str, object] = {}
        if mandate_id is not None:
            params["mandateId"] = mandate_id
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def get_mandate_by_id(
        self, mandate_id: str, **extra: object
    ) -> _models.GetMandateByIdResponse:
        """
        Get Mandate by ID

        Fetches full details of a specific direct debit mandate using its mandateId.
        """
        path = f"/v1/direct-debits/{mandate_id}"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def create_a_direct_debit_mandate(
        self,
        customer_account_number,
        bank_code,
        customer_name,
        customer_account_name,
        amount,
        frequency,
        merchant_reference,
        start_date,
        end_date,
        customer_email,
        *,
        customer_address: object | None = None,
        narration: object | None = None,
        customer_phone_number: object | None = None,
        start_immediately: object | None = None,
        **extra: object,
    ) -> _models.CreateADirectDebitMandateResponse:
        """
        Create a Direct Debit Mandate

        Creates a new direct debit mandate for a customer.

        Body fields:
            customerAccountNumber (required):
            bankCode (required):
            customerName (required):
            customerAccountName (required):
            amount (required):
            frequency (required):
            merchantReference (required): A NUMERIC string (0-9) used to track a transaction. It must be unique per transaction.
            startDate (required):
            endDate (required):
            customerEmail (required):
            customerAddress:
            narration:
            customerPhoneNumber:
            startImmediately:
        """
        path = f"/v1/direct-debits"
        params = None
        body: dict[str, object] = {}
        body["customerAccountNumber"] = customer_account_number
        body["bankCode"] = bank_code
        body["customerName"] = customer_name
        body["customerAccountName"] = customer_account_name
        body["amount"] = amount
        body["frequency"] = frequency
        body["merchantReference"] = merchant_reference
        body["startDate"] = start_date
        body["endDate"] = end_date
        body["customerEmail"] = customer_email
        if customer_address is not None:
            body["customerAddress"] = customer_address
        if narration is not None:
            body["narration"] = narration
        if customer_phone_number is not None:
            body["customerPhoneNumber"] = customer_phone_number
        if start_immediately is not None:
            body["startImmediately"] = start_immediately
        body.update(extra)
        validate_body("post", "/v1/direct-debits", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]


class AsyncDirectDebits:
    """Async resource methods for the DirectDebits group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def get_mandates_by_filters(
        self,
        *,
        page: str,
        page_size: str,
        from_: str | None = None,
        to: str | None = None,
        status: str | None = None,
        **extra: object,
    ) -> _models.GetMandatesByFiltersResponse:
        """
        Get mandates by filters
        """
        path = f"/v1/direct-debits/mandates"
        params: dict[str, object] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if from_ is not None:
            params["from"] = from_
        if to is not None:
            params["to"] = to
        if status is not None:
            params["status"] = status
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def update_mandate_status(
        self, mandate_id, status, **extra: object
    ) -> _models.UpdateMandateStatusResponse:
        """
        Update mandate status

        Updates the status of a direct debit mandate (e.g., SUSPEND, ACTIVE).

        Body fields:
            mandateId (required): Unique identifier of the mandate
            status (required): New status of the mandate
        """
        path = f"/v1/direct-debits/update-status"
        params = None
        body: dict[str, object] = {}
        body["mandateId"] = mandate_id
        body["status"] = status
        body.update(extra)
        validate_body("put", "/v1/direct-debits/update-status", body)
        return await self._client.put(path, json=body, params=params)  # type: ignore[return-value]

    async def debit_a_mandate(
        self, mandate_id, amount, **extra: object
    ) -> _models.DebitAMandateResponse:
        """
        Debit a mandate

        Debits a customer's account using an active mandate.

        Body fields:
            mandateId (required): Unique identifier of the mandate to debit
            amount (required): Amount to be debited
        """
        path = f"/v1/direct-debits/debit-mandate"
        params = None
        body: dict[str, object] = {}
        body["mandateId"] = mandate_id
        body["amount"] = amount
        body.update(extra)
        validate_body("post", "/v1/direct-debits/debit-mandate", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def get_mandate_status(
        self, *, mandate_id: str, **extra: object
    ) -> _models.GetMandateStatusResponse:
        """
        Get Mandate Status

        Fetches the status of a specific mandate by mandateId.
        """
        path = f"/v1/direct-debits/status?mandateId={mandate_id}"
        params: dict[str, object] = {}
        if mandate_id is not None:
            params["mandateId"] = mandate_id
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def get_mandate_by_id(
        self, mandate_id: str, **extra: object
    ) -> _models.GetMandateByIdResponse:
        """
        Get Mandate by ID

        Fetches full details of a specific direct debit mandate using its mandateId.
        """
        path = f"/v1/direct-debits/{mandate_id}"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def create_a_direct_debit_mandate(
        self,
        customer_account_number,
        bank_code,
        customer_name,
        customer_account_name,
        amount,
        frequency,
        merchant_reference,
        start_date,
        end_date,
        customer_email,
        *,
        customer_address: object | None = None,
        narration: object | None = None,
        customer_phone_number: object | None = None,
        start_immediately: object | None = None,
        **extra: object,
    ) -> _models.CreateADirectDebitMandateResponse:
        """
        Create a Direct Debit Mandate

        Creates a new direct debit mandate for a customer.

        Body fields:
            customerAccountNumber (required):
            bankCode (required):
            customerName (required):
            customerAccountName (required):
            amount (required):
            frequency (required):
            merchantReference (required): A NUMERIC string (0-9) used to track a transaction. It must be unique per transaction.
            startDate (required):
            endDate (required):
            customerEmail (required):
            customerAddress:
            narration:
            customerPhoneNumber:
            startImmediately:
        """
        path = f"/v1/direct-debits"
        params = None
        body: dict[str, object] = {}
        body["customerAccountNumber"] = customer_account_number
        body["bankCode"] = bank_code
        body["customerName"] = customer_name
        body["customerAccountName"] = customer_account_name
        body["amount"] = amount
        body["frequency"] = frequency
        body["merchantReference"] = merchant_reference
        body["startDate"] = start_date
        body["endDate"] = end_date
        body["customerEmail"] = customer_email
        if customer_address is not None:
            body["customerAddress"] = customer_address
        if narration is not None:
            body["narration"] = narration
        if customer_phone_number is not None:
            body["customerPhoneNumber"] = customer_phone_number
        if start_immediately is not None:
            body["startImmediately"] = start_immediately
        body.update(extra)
        validate_body("post", "/v1/direct-debits", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]
