# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations


from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class Electricity:
    """Sync resource methods for the Electricity group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def fetch_electricity_providers(self, **extra: object) -> _models.FetchElectricityProvidersResponse:
        """
        Fetch discos/electricity providers

        You can use this endpoint to fetch electricity providers/discos
        """
        path = "/v1/bill/electricity/discos"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def electricity_customer_lookup(self, *, disco: str | None = None, customer_id: str | None = None, **extra: object) -> _models.ElectricityCustomerLookupResponse:
        """
        Fetch customer information from an electricity provider

        This endpoint is for fetching customer information data from an electricity vending provider
        """
        path = "/v1/bill/electricity/lookup"
        params: dict[str, object] = {}
        if disco is not None:
            params["disco"] = disco
        if customer_id is not None:
            params["customerId"] = customer_id
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def vend_electricity_via_parent_account(self, *, disco: object | None = None, merchant_tx_ref: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, meter_type: object | None = None, **extra: object) -> _models.VendElectricityViaParentAccountResponse:
        """
        Vend electricity via parent account

        You can use this endpoint to vend electricity via parent account

        Body fields:
            disco: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            payerName: 
            amount: 
            customerId: 
            meterType: 
        """
        path = "/v1/bill/electricity"
        params = None
        body: dict[str, object] = {}
        if disco is not None:
            body["disco"] = disco
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        if meter_type is not None:
            body["meterType"] = meter_type
        body.update(extra)
        validate_body("post", "/v1/bill/electricity", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def vend_electricity_via_a_sub_account(self, sub_account_id: str, *, disco: object | None = None, merchant_tx_ref: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, meter_type: object | None = None, **extra: object) -> _models.VendElectricityViaASubAccountResponse:
        """
        Vend electricity via a specific account

        You can use this endpoint to vend electricity via a sub account

        Body fields:
            disco: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            payerName: 
            amount: 
            customerId: 
            meterType: 
        """
        path = f"/v1/bill/electricity/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        if disco is not None:
            body["disco"] = disco
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        if meter_type is not None:
            body["meterType"] = meter_type
        body.update(extra)
        validate_body("post", "/v1/bill/electricity/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]



class AsyncElectricity:
    """Async resource methods for the Electricity group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def fetch_electricity_providers(self, **extra: object) -> _models.FetchElectricityProvidersResponse:
        """
        Fetch discos/electricity providers

        You can use this endpoint to fetch electricity providers/discos
        """
        path = "/v1/bill/electricity/discos"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def electricity_customer_lookup(self, *, disco: str | None = None, customer_id: str | None = None, **extra: object) -> _models.ElectricityCustomerLookupResponse:
        """
        Fetch customer information from an electricity provider

        This endpoint is for fetching customer information data from an electricity vending provider
        """
        path = "/v1/bill/electricity/lookup"
        params: dict[str, object] = {}
        if disco is not None:
            params["disco"] = disco
        if customer_id is not None:
            params["customerId"] = customer_id
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def vend_electricity_via_parent_account(self, *, disco: object | None = None, merchant_tx_ref: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, meter_type: object | None = None, **extra: object) -> _models.VendElectricityViaParentAccountResponse:
        """
        Vend electricity via parent account

        You can use this endpoint to vend electricity via parent account

        Body fields:
            disco: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            payerName: 
            amount: 
            customerId: 
            meterType: 
        """
        path = "/v1/bill/electricity"
        params = None
        body: dict[str, object] = {}
        if disco is not None:
            body["disco"] = disco
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        if meter_type is not None:
            body["meterType"] = meter_type
        body.update(extra)
        validate_body("post", "/v1/bill/electricity", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def vend_electricity_via_a_sub_account(self, sub_account_id: str, *, disco: object | None = None, merchant_tx_ref: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, meter_type: object | None = None, **extra: object) -> _models.VendElectricityViaASubAccountResponse:
        """
        Vend electricity via a specific account

        You can use this endpoint to vend electricity via a sub account

        Body fields:
            disco: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            payerName: 
            amount: 
            customerId: 
            meterType: 
        """
        path = f"/v1/bill/electricity/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        if disco is not None:
            body["disco"] = disco
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        if meter_type is not None:
            body["meterType"] = meter_type
        body.update(extra)
        validate_body("post", "/v1/bill/electricity/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

