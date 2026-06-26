# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations

from typing import Any

from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class Betting:
    """Sync resource methods for the Betting group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def fetch_betting_providers(self, **extra: object) -> _models.FetchBettingProvidersResponse:
        """
        Fetch betting providers

        You can use this endpoint to fetch betting providers
        """
        path = f"/v1/bill/betting/providers"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def betting_customer_lookup(self, *, provider_id: str | None = None, customer_id: str | None = None, **extra: object) -> _models.BettingCustomerLookupResponse:
        """
        Fetch customer information from a betting provider

        This endpoint is for fetching customer information data from a bet vending provider
        """
        path = f"/v1/bill/betting/lookup"
        params: dict[str, object] = {}
        if provider_id is not None:
            params["providerId"] = provider_id
        if customer_id is not None:
            params["customerId"] = customer_id
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def vend_betting_via_parent_account(self, *, betting_provider: object | None = None, merchant_tx_ref: object | None = None, phone_number: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, **extra: object) -> _models.VendBettingViaParentAccountResponse:
        """
        Vend betting via parent account

        You can use this endpoint to vend betting via parent account

        Body fields:
            bettingProvider: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            phoneNumber: 
            payerName: 
            amount: 
            customerId: 
        """
        path = f"/v1/bill/betting"
        params = None
        body: dict[str, object] = {}
        if betting_provider is not None:
            body["bettingProvider"] = betting_provider
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if phone_number is not None:
            body["phoneNumber"] = phone_number
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        body.update(extra)
        validate_body("post", "/v1/bill/betting", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def vend_betting_via_a_sub_account(self, sub_account_id: str, *, betting_provider: object | None = None, merchant_tx_ref: object | None = None, phone_number: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, **extra: object) -> _models.VendBettingViaASubAccountResponse:
        """
        Vend betting via a specific account

        You can use this endpoint to vend betting via a sub account

        Body fields:
            bettingProvider: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            phoneNumber: 
            payerName: 
            amount: 
            customerId: 
        """
        path = f"/v1/bill/betting/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        if betting_provider is not None:
            body["bettingProvider"] = betting_provider
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if phone_number is not None:
            body["phoneNumber"] = phone_number
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        body.update(extra)
        validate_body("post", "/v1/bill/betting/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]



class AsyncBetting:
    """Async resource methods for the Betting group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def fetch_betting_providers(self, **extra: object) -> _models.FetchBettingProvidersResponse:
        """
        Fetch betting providers

        You can use this endpoint to fetch betting providers
        """
        path = f"/v1/bill/betting/providers"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def betting_customer_lookup(self, *, provider_id: str | None = None, customer_id: str | None = None, **extra: object) -> _models.BettingCustomerLookupResponse:
        """
        Fetch customer information from a betting provider

        This endpoint is for fetching customer information data from a bet vending provider
        """
        path = f"/v1/bill/betting/lookup"
        params: dict[str, object] = {}
        if provider_id is not None:
            params["providerId"] = provider_id
        if customer_id is not None:
            params["customerId"] = customer_id
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def vend_betting_via_parent_account(self, *, betting_provider: object | None = None, merchant_tx_ref: object | None = None, phone_number: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, **extra: object) -> _models.VendBettingViaParentAccountResponse:
        """
        Vend betting via parent account

        You can use this endpoint to vend betting via parent account

        Body fields:
            bettingProvider: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            phoneNumber: 
            payerName: 
            amount: 
            customerId: 
        """
        path = f"/v1/bill/betting"
        params = None
        body: dict[str, object] = {}
        if betting_provider is not None:
            body["bettingProvider"] = betting_provider
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if phone_number is not None:
            body["phoneNumber"] = phone_number
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        body.update(extra)
        validate_body("post", "/v1/bill/betting", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def vend_betting_via_a_sub_account(self, sub_account_id: str, *, betting_provider: object | None = None, merchant_tx_ref: object | None = None, phone_number: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, **extra: object) -> _models.VendBettingViaASubAccountResponse:
        """
        Vend betting via a specific account

        You can use this endpoint to vend betting via a sub account

        Body fields:
            bettingProvider: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            phoneNumber: 
            payerName: 
            amount: 
            customerId: 
        """
        path = f"/v1/bill/betting/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        if betting_provider is not None:
            body["bettingProvider"] = betting_provider
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if phone_number is not None:
            body["phoneNumber"] = phone_number
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        body.update(extra)
        validate_body("post", "/v1/bill/betting/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

