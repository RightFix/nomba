# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations

from typing import Any

from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class Checkout:
    """Sync resource methods for the Checkout group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def create_an_online_checkout_order(self, order, *, tokenize_card: object | None = None, **extra: object) -> _models.CreateAnOnlineCheckoutOrderResponse:
        """
        Create an online checkout order

        You can use this endpoint to create an online checkout order. Load the URL returned in 'checkoutLink' property in a browser to allow your customer initiate payment.

        Body fields:
            order (required): 
            tokenizeCard: Determines if the card used for payment is to be tokenized
        """
        path = f"/v1/checkout/order"
        params = None
        body: dict[str, object] = {}
        body["order"] = order
        if tokenize_card is not None:
            body["tokenizeCard"] = tokenize_card
        body.update(extra)
        validate_body("post", "/v1/checkout/order", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def charge_customer_with_tokenized_card_data(self, token_key, *, order: object | None = None, **extra: object) -> _models.ChargeCustomerWithTokenizedCardDataResponse:
        """
        Charge a customer using tokenized card data

        You can use this endpoint to charge a customer's card using the tokenized card details.

        Body fields:
            tokenKey (required): the token key returned in the webhook
            order: 
        """
        path = f"/v1/checkout/tokenized-card-payment"
        params = None
        body: dict[str, object] = {}
        body["tokenKey"] = token_key
        if order is not None:
            body["order"] = order
        body.update(extra)
        validate_body("post", "/v1/checkout/tokenized-card-payment", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def list_all_tokenized_cards_for_merchant(self, *, customer_email: str | None = None, start_date: str | None = None, end_date: str | None = None, page: str | None = None, **extra: object) -> _models.ListAllTokenizedCardsForMerchantResponse:
        """
        List tokenized cards

        Fetch list of merchant's tokenized cards
        """
        path = f"/v1/checkout/tokenized-card-data"
        params: dict[str, object] = {}
        if customer_email is not None:
            params["customerEmail"] = customer_email
        if start_date is not None:
            params["startDate"] = start_date
        if end_date is not None:
            params["endDate"] = end_date
        if page is not None:
            params["page"] = page
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def update_tokenized_card_data(self, token_key, current_email_address, new_email_address, **extra: object) -> _models.UpdateTokenizedCardDataResponse:
        """
        Update tokenized card data

        Update a tokenized card details

        Body fields:
            tokenKey (required): token key
            currentEmailAddress (required): customer email currently associated with the key
            newEmailAddress (required): new email to replace the old one
        """
        path = f"/v1/checkout/tokenized-card-data"
        params = None
        body: dict[str, object] = {}
        body["tokenKey"] = token_key
        body["currentEmailAddress"] = current_email_address
        body["newEmailAddress"] = new_email_address
        body.update(extra)
        validate_body("post", "/v1/checkout/tokenized-card-data", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def delete_tokenized_card_data(self, token_key, **extra: object) -> _models.DeleteTokenizedCardDataResponse:
        """
        Delete tokenized card data

        Delete a tokenized card details

        Body fields:
            tokenKey (required): token key
        """
        path = f"/v1/checkout/tokenized-card-data"
        params = None
        body: dict[str, object] = {}
        body["tokenKey"] = token_key
        body.update(extra)
        validate_body("delete", "/v1/checkout/tokenized-card-data", body)
        return self._client.delete(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_a_checkout_transaction(self, *, id_type: str | None = None, id: str | None = None, **extra: object) -> _models.FetchACheckoutTransactionResponse:
        """
        Fetch checkout transaction
        """
        path = f"/v1/checkout/transaction"
        params: dict[str, object] = {}
        if id_type is not None:
            params["idType"] = id_type
        if id is not None:
            params["id"] = id
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def refund_checkout_transaction(self, transaction_id, *, amount: object | None = None, account_number: object | None = None, bank_code: object | None = None, **extra: object) -> _models.RefundCheckoutTransactionResponse:
        """
        Refund checkout transaction

        You can use this endpoint to refund a checkout transaction.

        Body fields:
            transactionId (required): The ID of the transaction to be refunded
            amount: The amount to be refunded
            accountNumber: The account number for the refund
            bankCode: The bank code for the refund
        """
        path = f"/v1/checkout/refund"
        params = None
        body: dict[str, object] = {}
        body["transactionId"] = transaction_id
        if amount is not None:
            body["amount"] = amount
        if account_number is not None:
            body["accountNumber"] = account_number
        if bank_code is not None:
            body["bankCode"] = bank_code
        body.update(extra)
        validate_body("post", "/v1/checkout/refund", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def cancel_checkout_order(self, order_reference, **extra: object) -> _models.CancelCheckoutOrderResponse:
        """
        Cancel Checkout Order

        Use this endpoint to cancel an incomplete or pending checkout order.

        Body fields:
            orderReference (required): The unique reference of the checkout order to cancel
        """
        path = f"/v1/checkout/order/cancel"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body.update(extra)
        validate_body("post", "/v1/checkout/order/cancel", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]



class AsyncCheckout:
    """Async resource methods for the Checkout group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def create_an_online_checkout_order(self, order, *, tokenize_card: object | None = None, **extra: object) -> _models.CreateAnOnlineCheckoutOrderResponse:
        """
        Create an online checkout order

        You can use this endpoint to create an online checkout order. Load the URL returned in 'checkoutLink' property in a browser to allow your customer initiate payment.

        Body fields:
            order (required): 
            tokenizeCard: Determines if the card used for payment is to be tokenized
        """
        path = f"/v1/checkout/order"
        params = None
        body: dict[str, object] = {}
        body["order"] = order
        if tokenize_card is not None:
            body["tokenizeCard"] = tokenize_card
        body.update(extra)
        validate_body("post", "/v1/checkout/order", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def charge_customer_with_tokenized_card_data(self, token_key, *, order: object | None = None, **extra: object) -> _models.ChargeCustomerWithTokenizedCardDataResponse:
        """
        Charge a customer using tokenized card data

        You can use this endpoint to charge a customer's card using the tokenized card details.

        Body fields:
            tokenKey (required): the token key returned in the webhook
            order: 
        """
        path = f"/v1/checkout/tokenized-card-payment"
        params = None
        body: dict[str, object] = {}
        body["tokenKey"] = token_key
        if order is not None:
            body["order"] = order
        body.update(extra)
        validate_body("post", "/v1/checkout/tokenized-card-payment", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def list_all_tokenized_cards_for_merchant(self, *, customer_email: str | None = None, start_date: str | None = None, end_date: str | None = None, page: str | None = None, **extra: object) -> _models.ListAllTokenizedCardsForMerchantResponse:
        """
        List tokenized cards

        Fetch list of merchant's tokenized cards
        """
        path = f"/v1/checkout/tokenized-card-data"
        params: dict[str, object] = {}
        if customer_email is not None:
            params["customerEmail"] = customer_email
        if start_date is not None:
            params["startDate"] = start_date
        if end_date is not None:
            params["endDate"] = end_date
        if page is not None:
            params["page"] = page
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def update_tokenized_card_data(self, token_key, current_email_address, new_email_address, **extra: object) -> _models.UpdateTokenizedCardDataResponse:
        """
        Update tokenized card data

        Update a tokenized card details

        Body fields:
            tokenKey (required): token key
            currentEmailAddress (required): customer email currently associated with the key
            newEmailAddress (required): new email to replace the old one
        """
        path = f"/v1/checkout/tokenized-card-data"
        params = None
        body: dict[str, object] = {}
        body["tokenKey"] = token_key
        body["currentEmailAddress"] = current_email_address
        body["newEmailAddress"] = new_email_address
        body.update(extra)
        validate_body("post", "/v1/checkout/tokenized-card-data", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def delete_tokenized_card_data(self, token_key, **extra: object) -> _models.DeleteTokenizedCardDataResponse:
        """
        Delete tokenized card data

        Delete a tokenized card details

        Body fields:
            tokenKey (required): token key
        """
        path = f"/v1/checkout/tokenized-card-data"
        params = None
        body: dict[str, object] = {}
        body["tokenKey"] = token_key
        body.update(extra)
        validate_body("delete", "/v1/checkout/tokenized-card-data", body)
        return await self._client.delete(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_a_checkout_transaction(self, *, id_type: str | None = None, id: str | None = None, **extra: object) -> _models.FetchACheckoutTransactionResponse:
        """
        Fetch checkout transaction
        """
        path = f"/v1/checkout/transaction"
        params: dict[str, object] = {}
        if id_type is not None:
            params["idType"] = id_type
        if id is not None:
            params["id"] = id
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def refund_checkout_transaction(self, transaction_id, *, amount: object | None = None, account_number: object | None = None, bank_code: object | None = None, **extra: object) -> _models.RefundCheckoutTransactionResponse:
        """
        Refund checkout transaction

        You can use this endpoint to refund a checkout transaction.

        Body fields:
            transactionId (required): The ID of the transaction to be refunded
            amount: The amount to be refunded
            accountNumber: The account number for the refund
            bankCode: The bank code for the refund
        """
        path = f"/v1/checkout/refund"
        params = None
        body: dict[str, object] = {}
        body["transactionId"] = transaction_id
        if amount is not None:
            body["amount"] = amount
        if account_number is not None:
            body["accountNumber"] = account_number
        if bank_code is not None:
            body["bankCode"] = bank_code
        body.update(extra)
        validate_body("post", "/v1/checkout/refund", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def cancel_checkout_order(self, order_reference, **extra: object) -> _models.CancelCheckoutOrderResponse:
        """
        Cancel Checkout Order

        Use this endpoint to cancel an incomplete or pending checkout order.

        Body fields:
            orderReference (required): The unique reference of the checkout order to cancel
        """
        path = f"/v1/checkout/order/cancel"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body.update(extra)
        validate_body("post", "/v1/checkout/order/cancel", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

