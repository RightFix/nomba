# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations


from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class CableTv:
    """Sync resource methods for the CableTv group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def cabletv_lookup(self, *, customer_id: str | None = None, cable_tv_type: str | None = None, **extra: object) -> _models.CabletvLookupResponse:
        """
        Fetch customer information from a cable tv provider

        This endpoint is for fetching customer information data
        """
        path = "/v1/bill/cabletv/lookup"
        params: dict[str, object] = {}
        if customer_id is not None:
            params["customerId"] = customer_id
        if cable_tv_type is not None:
            params["cableTvType"] = cable_tv_type
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def cable_tv_subscription_via_parent_account(self, *, cable_tv_type: object | None = None, merchant_tx_ref: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, **extra: object) -> _models.CableTvSubscriptionViaParentAccountResponse:
        """
        CableTv subscription via parent account

        You can use this endpoint to make cable tv subscription via parent account

        Body fields:
            cableTvType: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            payerName: 
            amount: 
            customerId: 
        """
        path = "/v1/bill/cabletv"
        params = None
        body: dict[str, object] = {}
        if cable_tv_type is not None:
            body["cableTvType"] = cable_tv_type
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        body.update(extra)
        validate_body("post", "/v1/bill/cabletv", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def cable_tv_subscription_via_a_sub_account(self, sub_account_id: str, *, cable_tv_type: object | None = None, merchant_tx_ref: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, **extra: object) -> _models.CableTvSubscriptionViaASubAccountResponse:
        """
        CableTv subscription via a sub account

        You can use this endpoint to make cable tv subscription via a sub account

        Body fields:
            cableTvType: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            payerName: 
            amount: 
            customerId: 
        """
        path = f"/v1/bill/cabletv/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        if cable_tv_type is not None:
            body["cableTvType"] = cable_tv_type
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        body.update(extra)
        validate_body("post", "/v1/bill/cabletv/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]



class AsyncCableTv:
    """Async resource methods for the CableTv group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def cabletv_lookup(self, *, customer_id: str | None = None, cable_tv_type: str | None = None, **extra: object) -> _models.CabletvLookupResponse:
        """
        Fetch customer information from a cable tv provider

        This endpoint is for fetching customer information data
        """
        path = "/v1/bill/cabletv/lookup"
        params: dict[str, object] = {}
        if customer_id is not None:
            params["customerId"] = customer_id
        if cable_tv_type is not None:
            params["cableTvType"] = cable_tv_type
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def cable_tv_subscription_via_parent_account(self, *, cable_tv_type: object | None = None, merchant_tx_ref: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, **extra: object) -> _models.CableTvSubscriptionViaParentAccountResponse:
        """
        CableTv subscription via parent account

        You can use this endpoint to make cable tv subscription via parent account

        Body fields:
            cableTvType: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            payerName: 
            amount: 
            customerId: 
        """
        path = "/v1/bill/cabletv"
        params = None
        body: dict[str, object] = {}
        if cable_tv_type is not None:
            body["cableTvType"] = cable_tv_type
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        body.update(extra)
        validate_body("post", "/v1/bill/cabletv", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def cable_tv_subscription_via_a_sub_account(self, sub_account_id: str, *, cable_tv_type: object | None = None, merchant_tx_ref: object | None = None, payer_name: object | None = None, amount: object | None = None, customer_id: object | None = None, **extra: object) -> _models.CableTvSubscriptionViaASubAccountResponse:
        """
        CableTv subscription via a sub account

        You can use this endpoint to make cable tv subscription via a sub account

        Body fields:
            cableTvType: 
            merchantTxRef: This is an idempotency key and must be unique per transaction.
            payerName: 
            amount: 
            customerId: 
        """
        path = f"/v1/bill/cabletv/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        if cable_tv_type is not None:
            body["cableTvType"] = cable_tv_type
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if payer_name is not None:
            body["payerName"] = payer_name
        if amount is not None:
            body["amount"] = amount
        if customer_id is not None:
            body["customerId"] = customer_id
        body.update(extra)
        validate_body("post", "/v1/bill/cabletv/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

