# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations

from typing import Any

from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class GlobalCollections:
    """Sync resource methods for the GlobalCollections group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def initiate_mobile_money_inflow(self, phone_number, callback_url, amount, currency, topup_vendor, *, idempotency_key: object | None = None, **extra: object) -> _models.InitiateMobileMoneyInflowResponse:
        """

        Trigger a mobile money collection request from a customer.

        Body fields:
            phoneNumber (required): 
            callbackUrl (required): 
            amount (required): 
            currency (required): 
            topupVendor (required): Mobile money network provider (e.g. AIRTEL, MPESA).
            idempotencyKey: A client-generated key used to safely retry the request without risk of duplicate charges. If not provided, the server generates one automatically and returns it in the response.
        """
        path = f"/v1/global-collection/inflow/initiate"
        params = None
        body: dict[str, object] = {}
        body["phoneNumber"] = phone_number
        body["callbackUrl"] = callback_url
        body["amount"] = amount
        body["currency"] = currency
        body["topupVendor"] = topup_vendor
        if idempotency_key is not None:
            body["idempotencyKey"] = idempotency_key
        body.update(extra)
        validate_body("post", "/v1/global-collection/inflow/initiate", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_collection_transaction(self, transaction_id: str, **extra: object) -> _models.FetchCollectionTransactionResponse:
        """

        Retrieve the status of an initiated mobile money collection.
        """
        path = f"/v1/global-collection/transactions/{transaction_id}"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_drc_inflow_providers(self, **extra: object) -> _models.FetchDrcInflowProvidersResponse:
        """

        Returns the list of mobile money providers supported for DRC inflow. Use the returned code values as the topupVendor in the Initiate Mobile Money Inflow request.
        """
        path = f"/v1/global-collection/drc/inflow/providers"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_drc_inflow_providers_sandbox(self, **extra: object) -> _models.FetchDrcInflowProvidersSandboxResponse:
        """

        Sandbox version of Fetch DRC Inflow Providers. Returns the same static list of mobile money providers supported for DRC inflow for use in testing.
        """
        path = f"/v1/sandbox/global-collection/drc/inflow/providers"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]



class AsyncGlobalCollections:
    """Async resource methods for the GlobalCollections group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def initiate_mobile_money_inflow(self, phone_number, callback_url, amount, currency, topup_vendor, *, idempotency_key: object | None = None, **extra: object) -> _models.InitiateMobileMoneyInflowResponse:
        """

        Trigger a mobile money collection request from a customer.

        Body fields:
            phoneNumber (required): 
            callbackUrl (required): 
            amount (required): 
            currency (required): 
            topupVendor (required): Mobile money network provider (e.g. AIRTEL, MPESA).
            idempotencyKey: A client-generated key used to safely retry the request without risk of duplicate charges. If not provided, the server generates one automatically and returns it in the response.
        """
        path = f"/v1/global-collection/inflow/initiate"
        params = None
        body: dict[str, object] = {}
        body["phoneNumber"] = phone_number
        body["callbackUrl"] = callback_url
        body["amount"] = amount
        body["currency"] = currency
        body["topupVendor"] = topup_vendor
        if idempotency_key is not None:
            body["idempotencyKey"] = idempotency_key
        body.update(extra)
        validate_body("post", "/v1/global-collection/inflow/initiate", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_collection_transaction(self, transaction_id: str, **extra: object) -> _models.FetchCollectionTransactionResponse:
        """

        Retrieve the status of an initiated mobile money collection.
        """
        path = f"/v1/global-collection/transactions/{transaction_id}"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_drc_inflow_providers(self, **extra: object) -> _models.FetchDrcInflowProvidersResponse:
        """

        Returns the list of mobile money providers supported for DRC inflow. Use the returned code values as the topupVendor in the Initiate Mobile Money Inflow request.
        """
        path = f"/v1/global-collection/drc/inflow/providers"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_drc_inflow_providers_sandbox(self, **extra: object) -> _models.FetchDrcInflowProvidersSandboxResponse:
        """

        Sandbox version of Fetch DRC Inflow Providers. Returns the same static list of mobile money providers supported for DRC inflow for use in testing.
        """
        path = f"/v1/sandbox/global-collection/drc/inflow/providers"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

