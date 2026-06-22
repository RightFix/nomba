"""
Guided helper for Nomba's card-payment flow.

Nomba's card checkout is a multi-step sequence that otherwise requires
reading their docs to understand:

    1. Create an order                      -> orderReference
    2. Submit card details                  -> responseCode tells you what's next:
         "00" = done, payment completed
         "T0" = OTP required, call submit_otp()
         "S0" = 3D Secure required, redirect the user using secureAuthenticationData
    3. (if "T0") submit_otp(otp)            -> or resend_otp() if it didn't arrive
    4. confirm()                            -> final transaction status/details

This module wraps that sequence in a small stateful object so callers don't
need to track orderReference/transactionId by hand or look up what each
responseCode means.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..resources.charge import AsyncCharge, Charge
from .. import models as _models
# Response codes Nomba documents on the card-details submission response.
RESPONSE_CODE_SUCCESS = "00"
RESPONSE_CODE_OTP_REQUIRED = "T0"
RESPONSE_CODE_3DS_REQUIRED = "S0"


@dataclass
class CardPaymentStep:
    """Outcome of a single step in the card-payment flow."""

    raw: _models.SubmitCustomerCardDetailsResponse | _models.SubmitCustomerPaymentOtpResponse | dict[str, Any]
    response_code: str | None
    status: Any
    message: str | None
    transaction_id: str | None
    requires_otp: bool
    requires_3ds: bool
    secure_authentication_data: dict[str, Any] | None
    completed: bool


def _interpret(raw: _models.SubmitCustomerCardDetailsResponse | _models.SubmitCustomerPaymentOtpResponse, transaction_id_fallback: str | None = None) -> CardPaymentStep:
    data = raw.get("data", raw) if isinstance(raw.get("data"), dict) else raw
    response_code = data.get("responseCode")
    transaction_id = data.get("transactionId") or transaction_id_fallback
    return CardPaymentStep(
        raw=raw,
        response_code=response_code,
        status=data.get("status"),
        message=data.get("message"),
        transaction_id=transaction_id,
        requires_otp=response_code == RESPONSE_CODE_OTP_REQUIRED,
        requires_3ds=response_code == RESPONSE_CODE_3DS_REQUIRED,
        secure_authentication_data=data.get("secureAuthenticationData"),
        completed=response_code == RESPONSE_CODE_SUCCESS,
    )


class CardPaymentFlow:
    """
    Stateful, guided wrapper around Nomba's card-payment + OTP sequence.

    Example:
        from nomba import Nomba
        from nomba.flows import CardPaymentFlow

        nomba = Nomba(...)
        order = nomba.checkout.create_an_online_checkout_order(
            order={"orderReference": "order-001", "amount": "1000", ...}
        )
        order_ref = order["data"]["orderReference"]

        flow = CardPaymentFlow(nomba.charge, order_reference=order_ref)
        step = flow.submit_card(card_details="...", key="")

        if step.requires_otp:
            step = flow.submit_otp(otp="123456")
        elif step.requires_3ds:
            # redirect the user using step.secure_authentication_data
            ...

        if step.completed:
            result = flow.confirm()
    """

    def __init__(self, charge: "Charge", *, order_reference: str) -> None:
        self._charge = charge
        self.order_reference = order_reference
        self.transaction_id: str | None = None

    def submit_card(
        self,
        *,
        card_details: str,
        key: str = "",
        save_card: bool | None = None,
        device_information: object | None = None,
    ) -> CardPaymentStep:
        raw = self._charge.submit_customer_card_details(
            card_details=card_details,
            key=key,
            order_reference=self.order_reference,
            save_card=save_card,
            device_information=device_information,
        )
        step = _interpret(raw)
        self.transaction_id = step.transaction_id
        return step

    def submit_otp(self, otp: str) -> CardPaymentStep:
        if not self.transaction_id:
            raise ValueError(
                "No transaction_id on this flow yet — call submit_card() first."
            )
        raw = self._charge.submit_customer_payment_otp(
            otp=otp,
            order_reference=self.order_reference,
            transaction_id=self.transaction_id,
        )
        return _interpret(raw, transaction_id_fallback=self.transaction_id)

    def resend_otp(self) -> _models.ResendCustomerPaymentOtpResponse:
        return self._charge.resend_customer_payment_otp(
            order_reference=self.order_reference
        )

    def confirm(self) -> _models.FetchCheckoutTransactionDetailsResponse:
        return self._charge.fetch_checkout_transaction_details(
            order_reference=self.order_reference
        )

    def cancel(self, *, force: bool = False) -> _models.CancelCheckoutTransactionResponse:
        if not self.transaction_id:
            raise ValueError(
                "No transaction_id on this flow yet — call submit_card() first."
            )
        return self._charge.cancel_checkout_transaction(
            transaction_id=self.transaction_id, force_cancel=force
        )


class AsyncCardPaymentFlow:
    """Async version of `CardPaymentFlow` — same steps, all coroutines."""

    def __init__(self, charge: "AsyncCharge", *, order_reference: str) -> None:
        self._charge = charge
        self.order_reference = order_reference
        self.transaction_id: str | None = None

    async def submit_card(
        self,
        *,
        card_details: str,
        key: str = "",
        save_card: bool | None = None,
        device_information: object | None = None,
    ) -> CardPaymentStep:
        raw = await self._charge.submit_customer_card_details(
            card_details=card_details,
            key=key,
            order_reference=self.order_reference,
            save_card=save_card,
            device_information=device_information,
        )
        step = _interpret(raw)
        self.transaction_id = step.transaction_id
        return step

    async def submit_otp(self, otp: str) -> CardPaymentStep:
        if not self.transaction_id:
            raise ValueError(
                "No transaction_id on this flow yet — call submit_card() first."
            )
        raw = await self._charge.submit_customer_payment_otp(
            otp=otp,
            order_reference=self.order_reference,
            transaction_id=self.transaction_id,
        )
        return _interpret(raw, transaction_id_fallback=self.transaction_id)

    async def resend_otp(self)-> _models.ResendCustomerPaymentOtpResponse:
        return await self._charge.resend_customer_payment_otp(
            order_reference=self.order_reference
        )

    async def confirm(self)-> _models.FetchCheckoutTransactionDetailsResponse:
        return await self._charge.fetch_checkout_transaction_details(
            order_reference=self.order_reference
        )

    async def cancel(self, *, force: bool = False)-> _models.CancelCheckoutTransactionResponse:
        if not self.transaction_id:
            raise ValueError(
                "No transaction_id on this flow yet — call submit_card() first."
            )
        return await self._charge.cancel_checkout_transaction(
            transaction_id=self.transaction_id, force_cancel=force
        )
