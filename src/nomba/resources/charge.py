# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations


from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class Charge:
    """Sync resource methods for the Charge group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def fetch_checkout_order_details(self, order_reference: str, **extra: object) -> _models.FetchCheckoutOrderDetailsResponse:
        """
        Get Order details based on the generated Order reference

        Use this endpoint to fetch a single checkout order, using the order reference that was returned when the Order was created
        """
        path = f"/v1/checkout/order/{order_reference}"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def submit_customer_card_details(self, *, card_details: object | None = None, key: object | None = None, order_reference: object | None = None, save_card: object | None = None, device_information: object | None = None, **extra: object) -> _models.SubmitCustomerCardDetailsResponse:
        """
        Submit customer card details

        Use this endpoint to submit the customers card details

        Body fields:
            cardDetails: Stringified card details
            key: encryption key is data encrption is in use, else empty string
            orderReference: the order reference returned when the order was created
            saveCard: if true, this this user cardn will be saved for the user's future use. Note the process is not complete until the user-card verification endpoints are called to authenticate the user's phone number.
            deviceInformation: 
        """
        path = "/v1/checkout/checkout-card-detail"
        params = None
        body: dict[str, object] = {}
        if card_details is not None:
            body["cardDetails"] = card_details
        if key is not None:
            body["key"] = key
        if order_reference is not None:
            body["orderReference"] = order_reference
        if save_card is not None:
            body["saveCard"] = save_card
        if device_information is not None:
            body["deviceInformation"] = device_information
        body.update(extra)
        validate_body("post", "/v1/checkout/checkout-card-detail", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def submit_customer_payment_otp(self, otp, order_reference, transaction_id, **extra: object) -> _models.SubmitCustomerPaymentOtpResponse:
        """
        Submit customer card OTP

        Use this endpoint to submit the payment OTP sent to the customer's phones from the payment gateway

        Body fields:
            otp (required): otp send to the customer's mobile phone
            orderReference (required): order reference
            transactionId (required): transaction id returend when the card details were submitted
        """
        path = "/v1/checkout/checkout-card-otp"
        params = None
        body: dict[str, object] = {}
        body["otp"] = otp
        body["orderReference"] = order_reference
        body["transactionId"] = transaction_id
        body.update(extra)
        validate_body("post", "/v1/checkout/checkout-card-otp", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def resend_customer_payment_otp(self, order_reference, **extra: object) -> _models.ResendCustomerPaymentOtpResponse:
        """
        Resend OTP to customer's phone

        Use this endpoint to resend the payment OTP to the customer's phone

        Body fields:
            orderReference (required): order reference
        """
        path = "/v1/checkout/resend-otp"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body.update(extra)
        validate_body("post", "/v1/checkout/resend-otp", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_checkout_transaction_details(self, order_reference, **extra: object) -> _models.FetchCheckoutTransactionDetailsResponse:
        """
        Fetch checkout transaction details

        Use this endpoint to fetch the checkout transaction details and get the status of the transaction after OTP is submitted or transfer is made

        Body fields:
            orderReference (required): order reference
        """
        path = "/v1/checkout/confirm-transaction-receipt"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body.update(extra)
        validate_body("post", "/v1/checkout/confirm-transaction-receipt", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_checkout_flash_account_number(self, order_reference: str, **extra: object) -> _models.FetchCheckoutFlashAccountNumberResponse:
        """
        Fetch checkout Flash account number for transfer payment

        Use this endpoint to Get a flash account number which the customer cna use to make a transfer payment.
        """
        path = f"/v1/checkout/get-checkout-kta/{order_reference}"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def request_user_otp_to_authenticate_user(self, order_reference, phone_number, **extra: object) -> _models.RequestUserOtpToAuthenticateUserResponse:
        """
        Request OTP before saving a user's card

        Use this endpoint to request an OTP to be sent to be sent to the users phone number to authenticate the user before saving the card. This endpoint is called after payment is successful, and the user requested to save their card for later.

        Body fields:
            orderReference (required): order reference
            phoneNumber (required): customer's phone number
        """
        path = "/v1/checkout/user-card/auth"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body["phoneNumber"] = phone_number
        body.update(extra)
        validate_body("post", "/v1/checkout/user-card/auth", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def request_user_otp_to_authenticate_user_who_already_has_saved_cards(self, order_reference, **extra: object) -> _models.RequestUserOtpToAuthenticateUserWhoAlreadyHasSavedCardsResponse:
        """
        Request OTP to validate a user before fetching saved cards

        Use this endpoint to request an OTP to be sent to a user's phone number to authenticate before retrieving the saved cards mapped to the user's email. Use this endpoint when the Order details endpoint indicates the user already has saved cards.

        Body fields:
            orderReference (required): order reference
        """
        path = "/v1/checkout/user-card/saved-card/auth"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body.update(extra)
        validate_body("post", "/v1/checkout/user-card/saved-card/auth", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def submit_user_otp(self, order_reference, phone_number, otp, **extra: object) -> _models.SubmitUserOtpResponse:
        """
        Submit user OTP

        Use this endpoint to submit the user OTP send to the user's mobile number. This will result in the user's card being saved for later use.

        Body fields:
            orderReference (required): order reference
            phoneNumber (required): customer's phone number
            otp (required): otp send to the customer's mobile phone
        """
        path = "/v1/checkout/user-card"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body["phoneNumber"] = phone_number
        body["otp"] = otp
        body.update(extra)
        validate_body("post", "/v1/checkout/user-card", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_user_saved_cards(self, order_reference: str, *, otp: str, **extra: object) -> _models.FetchUserSavedCardsResponse:
        """
        Get user saved cards

        Use this endpoint to Get a user's saved cards. Requires user OTP send to the user after calling /checkout/user-card/saved-card/auth
        """
        path = f"/v1/checkout/user-card/{order_reference}"
        params: dict[str, object] = {}
        if otp is not None:
            params["otp"] = otp
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def cancel_checkout_transaction(self, transaction_id, force_cancel, **extra: object) -> _models.CancelCheckoutTransactionResponse:
        """
        Cancel Checkout transaction

        Use this endpoint to Cancel an incomplete checkout transaction

        Body fields:
            transactionId (required): the transaction Id returned when the card details were submitted
            forceCancel (required): Force the cancelation of the transaction
        """
        path = "/v1/checkout/transaction/cancel"
        params = None
        body: dict[str, object] = {}
        body["transactionId"] = transaction_id
        body["forceCancel"] = force_cancel
        body.update(extra)
        validate_body("post", "/v1/checkout/transaction/cancel", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]



class AsyncCharge:
    """Async resource methods for the Charge group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def fetch_checkout_order_details(self, order_reference: str, **extra: object) -> _models.FetchCheckoutOrderDetailsResponse:
        """
        Get Order details based on the generated Order reference

        Use this endpoint to fetch a single checkout order, using the order reference that was returned when the Order was created
        """
        path = f"/v1/checkout/order/{order_reference}"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def submit_customer_card_details(self, *, card_details: object | None = None, key: object | None = None, order_reference: object | None = None, save_card: object | None = None, device_information: object | None = None, **extra: object) -> _models.SubmitCustomerCardDetailsResponse:
        """
        Submit customer card details

        Use this endpoint to submit the customers card details

        Body fields:
            cardDetails: Stringified card details
            key: encryption key is data encrption is in use, else empty string
            orderReference: the order reference returned when the order was created
            saveCard: if true, this this user cardn will be saved for the user's future use. Note the process is not complete until the user-card verification endpoints are called to authenticate the user's phone number.
            deviceInformation: 
        """
        path = "/v1/checkout/checkout-card-detail"
        params = None
        body: dict[str, object] = {}
        if card_details is not None:
            body["cardDetails"] = card_details
        if key is not None:
            body["key"] = key
        if order_reference is not None:
            body["orderReference"] = order_reference
        if save_card is not None:
            body["saveCard"] = save_card
        if device_information is not None:
            body["deviceInformation"] = device_information
        body.update(extra)
        validate_body("post", "/v1/checkout/checkout-card-detail", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def submit_customer_payment_otp(self, otp, order_reference, transaction_id, **extra: object) -> _models.SubmitCustomerPaymentOtpResponse:
        """
        Submit customer card OTP

        Use this endpoint to submit the payment OTP sent to the customer's phones from the payment gateway

        Body fields:
            otp (required): otp send to the customer's mobile phone
            orderReference (required): order reference
            transactionId (required): transaction id returend when the card details were submitted
        """
        path = "/v1/checkout/checkout-card-otp"
        params = None
        body: dict[str, object] = {}
        body["otp"] = otp
        body["orderReference"] = order_reference
        body["transactionId"] = transaction_id
        body.update(extra)
        validate_body("post", "/v1/checkout/checkout-card-otp", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def resend_customer_payment_otp(self, order_reference, **extra: object) -> _models.ResendCustomerPaymentOtpResponse:
        """
        Resend OTP to customer's phone

        Use this endpoint to resend the payment OTP to the customer's phone

        Body fields:
            orderReference (required): order reference
        """
        path = "/v1/checkout/resend-otp"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body.update(extra)
        validate_body("post", "/v1/checkout/resend-otp", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_checkout_transaction_details(self, order_reference, **extra: object) -> _models.FetchCheckoutTransactionDetailsResponse:
        """
        Fetch checkout transaction details

        Use this endpoint to fetch the checkout transaction details and get the status of the transaction after OTP is submitted or transfer is made

        Body fields:
            orderReference (required): order reference
        """
        path = "/v1/checkout/confirm-transaction-receipt"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body.update(extra)
        validate_body("post", "/v1/checkout/confirm-transaction-receipt", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_checkout_flash_account_number(self, order_reference: str, **extra: object) -> _models.FetchCheckoutFlashAccountNumberResponse:
        """
        Fetch checkout Flash account number for transfer payment

        Use this endpoint to Get a flash account number which the customer cna use to make a transfer payment.
        """
        path = f"/v1/checkout/get-checkout-kta/{order_reference}"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def request_user_otp_to_authenticate_user(self, order_reference, phone_number, **extra: object) -> _models.RequestUserOtpToAuthenticateUserResponse:
        """
        Request OTP before saving a user's card

        Use this endpoint to request an OTP to be sent to be sent to the users phone number to authenticate the user before saving the card. This endpoint is called after payment is successful, and the user requested to save their card for later.

        Body fields:
            orderReference (required): order reference
            phoneNumber (required): customer's phone number
        """
        path = "/v1/checkout/user-card/auth"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body["phoneNumber"] = phone_number
        body.update(extra)
        validate_body("post", "/v1/checkout/user-card/auth", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def request_user_otp_to_authenticate_user_who_already_has_saved_cards(self, order_reference, **extra: object) -> _models.RequestUserOtpToAuthenticateUserWhoAlreadyHasSavedCardsResponse:
        """
        Request OTP to validate a user before fetching saved cards

        Use this endpoint to request an OTP to be sent to a user's phone number to authenticate before retrieving the saved cards mapped to the user's email. Use this endpoint when the Order details endpoint indicates the user already has saved cards.

        Body fields:
            orderReference (required): order reference
        """
        path = "/v1/checkout/user-card/saved-card/auth"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body.update(extra)
        validate_body("post", "/v1/checkout/user-card/saved-card/auth", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def submit_user_otp(self, order_reference, phone_number, otp, **extra: object) -> _models.SubmitUserOtpResponse:
        """
        Submit user OTP

        Use this endpoint to submit the user OTP send to the user's mobile number. This will result in the user's card being saved for later use.

        Body fields:
            orderReference (required): order reference
            phoneNumber (required): customer's phone number
            otp (required): otp send to the customer's mobile phone
        """
        path = "/v1/checkout/user-card"
        params = None
        body: dict[str, object] = {}
        body["orderReference"] = order_reference
        body["phoneNumber"] = phone_number
        body["otp"] = otp
        body.update(extra)
        validate_body("post", "/v1/checkout/user-card", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_user_saved_cards(self, order_reference: str, *, otp: str, **extra: object) -> _models.FetchUserSavedCardsResponse:
        """
        Get user saved cards

        Use this endpoint to Get a user's saved cards. Requires user OTP send to the user after calling /checkout/user-card/saved-card/auth
        """
        path = f"/v1/checkout/user-card/{order_reference}"
        params: dict[str, object] = {}
        if otp is not None:
            params["otp"] = otp
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def cancel_checkout_transaction(self, transaction_id, force_cancel, **extra: object) -> _models.CancelCheckoutTransactionResponse:
        """
        Cancel Checkout transaction

        Use this endpoint to Cancel an incomplete checkout transaction

        Body fields:
            transactionId (required): the transaction Id returned when the card details were submitted
            forceCancel (required): Force the cancelation of the transaction
        """
        path = "/v1/checkout/transaction/cancel"
        params = None
        body: dict[str, object] = {}
        body["transactionId"] = transaction_id
        body["forceCancel"] = force_cancel
        body.update(extra)
        validate_body("post", "/v1/checkout/transaction/cancel", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

