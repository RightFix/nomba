# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations


from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class AirtimeData:
    """Sync resource methods for the AirtimeData group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def fetch_data_plans_available_on_a_telco_network_provider(self, telco: str, **extra: object) -> _models.FetchDataPlansAvailableOnATelcoNetworkProviderResponse:
        """
        Fetch data plans available on a telco (network provider)

        You can use this endpoint to fetch data plans available on a telco (network provider)
        """
        path = f"/v1/bill/data-plan/{telco}"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def make_airtime_purchases_via_parent_account(self, amount, phone_number, network, merchant_tx_ref, *, sender_name: object | None = None, **extra: object) -> _models.MakeAirtimePurchasesViaParentAccountResponse:
        """
        Make airtime purchases via parent account

        You can use this endpoint to make airtime purchases via parent account

        Body fields:
            amount (required): The airtime amount to be purchased
            phoneNumber (required): Recipient phone number
            network (required): Recipient network (telco). It can also come as lowercased values e.g. glo, mtn etc.
            merchantTxRef (required): Merchant Transaction Identifier reference (Unique to merchant)
            senderName: A name to describe the sender of the airtime
        """
        path = "/v1/bill/topup"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["phoneNumber"] = phone_number
        body["network"] = network
        body["merchantTxRef"] = merchant_tx_ref
        if sender_name is not None:
            body["senderName"] = sender_name
        body.update(extra)
        validate_body("post", "/v1/bill/topup", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def make_airtime_purchases_via_specific_or_sub_account(self, sub_account_id: str, amount, phone_number, network, merchant_tx_ref, *, sender_name: object | None = None, **extra: object) -> _models.MakeAirtimePurchasesViaSpecificOrSubAccountResponse:
        """
        Make airtime purchases via a sub account

        You can use this endpoint to make airtime purchases via a sub account

        Body fields:
            amount (required): The airtime amount to be purchased
            phoneNumber (required): Recipient phone number
            network (required): Recipient network (telco). It can also come as lowercased values e.g. glo, mtn etc.
            merchantTxRef (required): Merchant Transaction Identifier reference (Unique to merchant)
            senderName: A name to describe the sender of the airtime
        """
        path = f"/v1/bill/topup/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["phoneNumber"] = phone_number
        body["network"] = network
        body["merchantTxRef"] = merchant_tx_ref
        if sender_name is not None:
            body["senderName"] = sender_name
        body.update(extra)
        validate_body("post", "/v1/bill/topup/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def vend_data_bundles_via_parent_account(self, amount, phone_number, network, merchant_tx_ref, *, sender_name: object | None = None, **extra: object) -> _models.VendDataBundlesViaParentAccountResponse:
        """
        Vend data bundles via parent account

        You can use this endpoint to vend data via parent account

        Body fields:
            amount (required): The data amount to be vended
            phoneNumber (required): Recipient phone number
            network (required): Recipient network (telco). It can also come as lowercased values e.g. glo, mtn etc.
            merchantTxRef (required): Merchant Transaction Identifier reference (Unique to merchant)
            senderName: A name to describe the sender of the data
        """
        path = "/v1/bill/data"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["phoneNumber"] = phone_number
        body["network"] = network
        body["merchantTxRef"] = merchant_tx_ref
        if sender_name is not None:
            body["senderName"] = sender_name
        body.update(extra)
        validate_body("post", "/v1/bill/data", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def vend_data_bundles_via_specific_or_sub_account(self, sub_account_id: str, amount, phone_number, network, merchant_tx_ref, *, sender_name: object | None = None, **extra: object) -> _models.VendDataBundlesViaSpecificOrSubAccountResponse:
        """
        Vend data bundles via a sub account

        You can use this endpoint to vend data via a sub account

        Body fields:
            amount (required): The data amount to be vended
            phoneNumber (required): Recipient phone number
            network (required): Recipient network (telco). It can also come as lowercased values e.g. glo, mtn etc.
            merchantTxRef (required): Merchant Transaction Identifier reference (Unique to merchant)
            senderName: A name to describe the sender of the data
        """
        path = f"/v1/bill/data/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["phoneNumber"] = phone_number
        body["network"] = network
        body["merchantTxRef"] = merchant_tx_ref
        if sender_name is not None:
            body["senderName"] = sender_name
        body.update(extra)
        validate_body("post", "/v1/bill/data/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]



class AsyncAirtimeData:
    """Async resource methods for the AirtimeData group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def fetch_data_plans_available_on_a_telco_network_provider(self, telco: str, **extra: object) -> _models.FetchDataPlansAvailableOnATelcoNetworkProviderResponse:
        """
        Fetch data plans available on a telco (network provider)

        You can use this endpoint to fetch data plans available on a telco (network provider)
        """
        path = f"/v1/bill/data-plan/{telco}"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def make_airtime_purchases_via_parent_account(self, amount, phone_number, network, merchant_tx_ref, *, sender_name: object | None = None, **extra: object) -> _models.MakeAirtimePurchasesViaParentAccountResponse:
        """
        Make airtime purchases via parent account

        You can use this endpoint to make airtime purchases via parent account

        Body fields:
            amount (required): The airtime amount to be purchased
            phoneNumber (required): Recipient phone number
            network (required): Recipient network (telco). It can also come as lowercased values e.g. glo, mtn etc.
            merchantTxRef (required): Merchant Transaction Identifier reference (Unique to merchant)
            senderName: A name to describe the sender of the airtime
        """
        path = "/v1/bill/topup"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["phoneNumber"] = phone_number
        body["network"] = network
        body["merchantTxRef"] = merchant_tx_ref
        if sender_name is not None:
            body["senderName"] = sender_name
        body.update(extra)
        validate_body("post", "/v1/bill/topup", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def make_airtime_purchases_via_specific_or_sub_account(self, sub_account_id: str, amount, phone_number, network, merchant_tx_ref, *, sender_name: object | None = None, **extra: object) -> _models.MakeAirtimePurchasesViaSpecificOrSubAccountResponse:
        """
        Make airtime purchases via a sub account

        You can use this endpoint to make airtime purchases via a sub account

        Body fields:
            amount (required): The airtime amount to be purchased
            phoneNumber (required): Recipient phone number
            network (required): Recipient network (telco). It can also come as lowercased values e.g. glo, mtn etc.
            merchantTxRef (required): Merchant Transaction Identifier reference (Unique to merchant)
            senderName: A name to describe the sender of the airtime
        """
        path = f"/v1/bill/topup/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["phoneNumber"] = phone_number
        body["network"] = network
        body["merchantTxRef"] = merchant_tx_ref
        if sender_name is not None:
            body["senderName"] = sender_name
        body.update(extra)
        validate_body("post", "/v1/bill/topup/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def vend_data_bundles_via_parent_account(self, amount, phone_number, network, merchant_tx_ref, *, sender_name: object | None = None, **extra: object) -> _models.VendDataBundlesViaParentAccountResponse:
        """
        Vend data bundles via parent account

        You can use this endpoint to vend data via parent account

        Body fields:
            amount (required): The data amount to be vended
            phoneNumber (required): Recipient phone number
            network (required): Recipient network (telco). It can also come as lowercased values e.g. glo, mtn etc.
            merchantTxRef (required): Merchant Transaction Identifier reference (Unique to merchant)
            senderName: A name to describe the sender of the data
        """
        path = "/v1/bill/data"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["phoneNumber"] = phone_number
        body["network"] = network
        body["merchantTxRef"] = merchant_tx_ref
        if sender_name is not None:
            body["senderName"] = sender_name
        body.update(extra)
        validate_body("post", "/v1/bill/data", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def vend_data_bundles_via_specific_or_sub_account(self, sub_account_id: str, amount, phone_number, network, merchant_tx_ref, *, sender_name: object | None = None, **extra: object) -> _models.VendDataBundlesViaSpecificOrSubAccountResponse:
        """
        Vend data bundles via a sub account

        You can use this endpoint to vend data via a sub account

        Body fields:
            amount (required): The data amount to be vended
            phoneNumber (required): Recipient phone number
            network (required): Recipient network (telco). It can also come as lowercased values e.g. glo, mtn etc.
            merchantTxRef (required): Merchant Transaction Identifier reference (Unique to merchant)
            senderName: A name to describe the sender of the data
        """
        path = f"/v1/bill/data/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["phoneNumber"] = phone_number
        body["network"] = network
        body["merchantTxRef"] = merchant_tx_ref
        if sender_name is not None:
            body["senderName"] = sender_name
        body.update(extra)
        validate_body("post", "/v1/bill/data/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

