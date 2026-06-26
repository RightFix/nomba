# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
#
# These TypedDicts describe the shape of each endpoint's response for
# editor autocomplete / type checking. They cost nothing at runtime --
# methods still return plain dicts; TypedDict is purely a type hint.
from __future__ import annotations

from typing import Any, TypedDict


class ListAllAccountsResponse(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class CreateASubAccountData(TypedDict, total=False):
    createdAt: str
    accountId: str
    accountHolderId: str
    accountRef: str
    phoneNumber: str
    email: str
    bvn: str
    status: str
    type: str
    accountName: str
    currency: str
    callbackUrl: str
    expiryDate: str

class CreateASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CreateASubAccountData

class FetchAccountDetailsData(TypedDict, total=False):
    createdAt: str
    accountId: str
    accountHolderId: str
    accountRef: str
    bvn: str
    status: str
    type: str
    accountName: str
    currency: str
    banks: list[dict[str, Any]]

class FetchAccountDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchAccountDetailsData

class FetchParentAccountDetailsData(TypedDict, total=False):
    createdAt: str
    accountId: str
    accountHolderId: str
    accountRef: str
    bvn: str
    status: str
    type: str
    accountName: str
    currency: str
    banks: list[dict[str, Any]]

class FetchParentAccountDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchParentAccountDetailsData

class FetchAccountBalanceData(TypedDict, total=False):
    amount: str
    currency: str
    timeCreated: str

class FetchAccountBalanceResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchAccountBalanceData

class FetchParentAccountBalanceData(TypedDict, total=False):
    amount: str
    currency: str
    timeCreated: str

class FetchParentAccountBalanceResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchParentAccountBalanceData

class SuspendAnAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class ReactivateASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class FetchTerminalsAssignedToAnAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTerminalsAssignedToAnAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTerminalsAssignedToAnAccountData

class FetchTerminalsAssignedToTheParentAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTerminalsAssignedToTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTerminalsAssignedToTheParentAccountData

class FetchTerminalsAssignedToASubAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTerminalsAssignedToASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTerminalsAssignedToASubAccountData

class UpdateAccessToAccountData(TypedDict, total=False):
    message: str
    data: dict[str, Any]

class UpdateAccessToAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: UpdateAccessToAccountData

class CreateVirtualAccountData(TypedDict, total=False):
    createdAt: str
    accountHolderId: str
    accountRef: str
    bvn: str
    accountName: str
    bankName: str
    bankAccountNumber: str
    bankAccountName: str
    currency: str
    callbackUrl: str
    expired: bool

class CreateVirtualAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CreateVirtualAccountData

class CreateVirtualAccountForASubAccountData(TypedDict, total=False):
    createdAt: str
    accountHolderId: str
    accountRef: str
    bvn: str
    accountName: str
    bankName: str
    bankAccountNumber: str
    bankAccountName: str
    currency: str
    callbackUrl: str
    expired: bool

class CreateVirtualAccountForASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CreateVirtualAccountForASubAccountData

class FilterVirtualAccountsData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FilterVirtualAccountsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FilterVirtualAccountsData

class UpdateAVirtualAccountData(TypedDict, total=False):
    updated: bool

class UpdateAVirtualAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: UpdateAVirtualAccountData

class FetchAVirtualAccountData(TypedDict, total=False):
    createdAt: str
    accountHolderId: str
    accountRef: str
    bvn: str
    accountName: str
    bankName: str
    bankAccountNumber: str
    bankAccountName: str
    currency: str
    callbackUrl: str
    expired: bool

class FetchAVirtualAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchAVirtualAccountData

class ExpireAVirtualAccountData(TypedDict, total=False):
    expired: bool

class ExpireAVirtualAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: ExpireAVirtualAccountData

class CreateAnOnlineCheckoutOrderData(TypedDict, total=False):
    checkoutLink: str
    orderReference: str

class CreateAnOnlineCheckoutOrderResponse(TypedDict, total=False):
    code: str
    description: str
    data: CreateAnOnlineCheckoutOrderData

class ChargeCustomerWithTokenizedCardDataData(TypedDict, total=False):
    status: bool
    message: str

class ChargeCustomerWithTokenizedCardDataResponse(TypedDict, total=False):
    code: str
    description: str
    data: ChargeCustomerWithTokenizedCardDataData

class ListAllTokenizedCardsForMerchantData(TypedDict, total=False):
    nextPage: str
    tokenizedCardDataList: list[dict[str, Any]]

class ListAllTokenizedCardsForMerchantResponse(TypedDict, total=False):
    code: str
    description: str
    data: ListAllTokenizedCardsForMerchantData

class UpdateTokenizedCardDataData(TypedDict, total=False):
    status: bool
    message: str
    tokenizedCardData: Any

class UpdateTokenizedCardDataResponse(TypedDict, total=False):
    code: str
    description: str
    data: UpdateTokenizedCardDataData

class DeleteTokenizedCardDataData(TypedDict, total=False):
    status: bool
    message: str

class DeleteTokenizedCardDataResponse(TypedDict, total=False):
    code: str
    description: str
    data: DeleteTokenizedCardDataData

class FetchACheckoutTransactionData(TypedDict, total=False):
    success: bool
    message: str
    order: dict[str, Any]
    transactionDetails: dict[str, Any]
    transferDetails: dict[str, Any]
    cardDetails: dict[str, Any]

class FetchACheckoutTransactionResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchACheckoutTransactionData

class RefundCheckoutTransactionData(TypedDict, total=False):
    success: bool
    message: str

class RefundCheckoutTransactionResponse(TypedDict, total=False):
    code: str
    description: str
    data: RefundCheckoutTransactionData

class FetchCheckoutOrderDetailsData(TypedDict, total=False):
    order: dict[str, Any]
    hasSavedCards: bool
    base64EncodedRsaPublicKey: str

class FetchCheckoutOrderDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCheckoutOrderDetailsData

class SubmitCustomerCardDetailsData(TypedDict, total=False):
    status: bool
    message: str
    responseCode: str
    transactionId: str
    secureAuthenticationData: dict[str, Any]

class SubmitCustomerCardDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: SubmitCustomerCardDetailsData

class SubmitCustomerPaymentOtpData(TypedDict, total=False):
    status: bool
    message: str

class SubmitCustomerPaymentOtpResponse(TypedDict, total=False):
    code: str
    description: str
    data: SubmitCustomerPaymentOtpData

class ResendCustomerPaymentOtpData(TypedDict, total=False):
    success: bool
    message: str

class ResendCustomerPaymentOtpResponse(TypedDict, total=False):
    code: str
    description: str
    data: ResendCustomerPaymentOtpData

class FetchCheckoutTransactionDetailsData(TypedDict, total=False):
    status: bool
    message: str
    order: dict[str, Any]

class FetchCheckoutTransactionDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCheckoutTransactionDetailsData

class FetchCheckoutFlashAccountNumberData(TypedDict, total=False):
    accountNumber: str
    accountName: str
    bankName: str

class FetchCheckoutFlashAccountNumberResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCheckoutFlashAccountNumberData

class RequestUserOtpToAuthenticateUserData(TypedDict, total=False):
    success: bool
    message: str

class RequestUserOtpToAuthenticateUserResponse(TypedDict, total=False):
    code: str
    description: str
    data: RequestUserOtpToAuthenticateUserData

class RequestUserOtpToAuthenticateUserWhoAlreadyHasSavedCardsData(TypedDict, total=False):
    success: bool
    message: str

class RequestUserOtpToAuthenticateUserWhoAlreadyHasSavedCardsResponse(TypedDict, total=False):
    code: str
    description: str
    data: RequestUserOtpToAuthenticateUserWhoAlreadyHasSavedCardsData

class SubmitUserOtpData(TypedDict, total=False):
    success: bool
    message: str

class SubmitUserOtpResponse(TypedDict, total=False):
    code: str
    description: str
    data: SubmitUserOtpData

class FetchUserSavedCardsData(TypedDict, total=False):
    tokenizedCardData: Any

class FetchUserSavedCardsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchUserSavedCardsData

class CancelCheckoutTransactionData(TypedDict, total=False):
    success: bool
    message: str

class CancelCheckoutTransactionResponse(TypedDict, total=False):
    code: str
    description: str
    data: CancelCheckoutTransactionData

class FetchBankCodesAndNamesData(TypedDict, total=False):
    results: list[dict[str, Any]]

class FetchBankCodesAndNamesResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchBankCodesAndNamesData

class PerformBankAccountLookupData(TypedDict, total=False):
    accountNumber: str
    accountName: str

class PerformBankAccountLookupResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformBankAccountLookupData

class PerformBankAccountTransferFromTheParentAccountData(TypedDict, total=False):
    amount: str
    source: str
    sourceUserId: str
    customerBillerId: str
    productId: str
    meta: dict[str, Any]
    fee: float
    timeCreated: str
    id: str
    type: str
    status: str

class PerformBankAccountTransferFromTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformBankAccountTransferFromTheParentAccountData

class PerformBankAccountTransferFromAccountData(TypedDict, total=False):
    amount: str
    source: str
    sourceUserId: str
    customerBillerId: str
    productId: str
    meta: dict[str, Any]
    fee: float
    timeCreated: str
    id: str
    type: str
    status: str

class PerformBankAccountTransferFromAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformBankAccountTransferFromAccountData

class PerformWalletTransferFromTheParentAccountData(TypedDict, total=False):
    amount: float
    meta: dict[str, Any]
    fee: float
    timeCreated: str
    id: str
    type: str
    status: str

class PerformWalletTransferFromTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformWalletTransferFromTheParentAccountData

class PerformWalletTransferFromASubAccountData(TypedDict, total=False):
    amount: float
    meta: dict[str, Any]
    fee: float
    timeCreated: str
    id: str
    type: str
    status: str

class PerformWalletTransferFromASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformWalletTransferFromASubAccountData

class AssignATerminalToAnAccountData(TypedDict, total=False):
    terminalId: str
    serialNumber: str
    accountId: str
    parentAccountId: str
    merchantName: str
    terminalLabel: str
    createdAt: str
    updatedAt: str

class AssignATerminalToAnAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: AssignATerminalToAnAccountData

class AssignATerminalToTheParentAccountData(TypedDict, total=False):
    terminalId: str
    serialNumber: str
    accountId: str
    parentAccountId: str
    merchantName: str
    terminalLabel: str
    createdAt: str
    updatedAt: str

class AssignATerminalToTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: AssignATerminalToTheParentAccountData

class UnAssignTerminalFromAnAccountData(TypedDict, total=False):
    terminalId: str
    serialNumber: str
    accountId: str
    parentAccountId: str
    merchantName: str
    terminalLabel: str
    createdAt: str
    updatedAt: str

class UnAssignTerminalFromAnAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: UnAssignTerminalFromAnAccountData

class UnAssignATerminalFromTheParentAccountData(TypedDict, total=False):
    terminalId: str
    serialNumber: str
    accountId: str
    parentAccountId: str
    merchantName: str
    terminalLabel: str
    createdAt: str
    updatedAt: str

class UnAssignATerminalFromTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: UnAssignATerminalFromTheParentAccountData

class SendPaymentRequestToTerminalData(TypedDict, total=False):
    paymentId: str
    status: str
    amount: float
    currency: str
    createdAt: str

class SendPaymentRequestToTerminalResponse(TypedDict, total=False):
    code: str
    description: str
    data: SendPaymentRequestToTerminalData

class FetchCreditDebitTransactionsOnASubAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchCreditDebitTransactionsOnASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCreditDebitTransactionsOnASubAccountData

class FetchCreditDebitTransactionsOnTheParentAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchCreditDebitTransactionsOnTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCreditDebitTransactionsOnTheParentAccountData

class FetchTransactionsOnASubAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTransactionsOnASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTransactionsOnASubAccountData

class FilterSubAccountTransactionsData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FilterSubAccountTransactionsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FilterSubAccountTransactionsData

class FetchTransactionsOnTheParentAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTransactionsOnTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTransactionsOnTheParentAccountData

class FilterParentAccountTransactionsData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FilterParentAccountTransactionsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FilterParentAccountTransactionsData

class FetchASingleTransactionOnASubAccountData(TypedDict, total=False):
    id: str
    status: str
    amount: float
    fixedCharge: float
    source: str
    type: str
    gatewayMessage: str
    customerBillerId: str
    timeCreated: str
    posTid: str
    terminalId: str
    providerTerminalId: str
    rrn: str
    posSerialNumber: str
    posTerminalLabel: str
    stan: str
    paymentVendorReference: str
    userId: str
    posRrn: str
    merchantTxRef: str

class FetchASingleTransactionOnASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchASingleTransactionOnASubAccountData

class FetchASingleTransactionOnTheParentAccountData(TypedDict, total=False):
    id: str
    status: str
    amount: float
    fixedCharge: float
    source: str
    type: str
    gatewayMessage: str
    customerBillerId: str
    timeCreated: str
    posTid: str
    terminalId: str
    providerTerminalId: str
    rrn: str
    posSerialNumber: str
    posTerminalLabel: str
    stan: str
    paymentVendorReference: str
    userId: str
    posRrn: str
    merchantTxRef: str

class FetchASingleTransactionOnTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchASingleTransactionOnTheParentAccountData

class ConfirmATransactionSStatusBySessionIdData(TypedDict, total=False):
    id: str
    status: str
    amount: float
    fixedCharge: float
    source: str
    type: str
    gatewayMessage: str
    customerBillerId: str
    timeCreated: str
    posTid: str
    terminalId: str
    providerTerminalId: str
    rrn: str
    posSerialNumber: str
    posTerminalLabel: str
    stan: str
    paymentVendorReference: str
    userId: str
    posRrn: str
    merchantTxRef: str

class ConfirmATransactionSStatusBySessionIdResponse(TypedDict, total=False):
    code: str
    description: str
    data: ConfirmATransactionSStatusBySessionIdData

class FetchDataPlansAvailableOnATelcoNetworkProviderData(TypedDict, total=False):
    amount: int
    plan: str

class FetchDataPlansAvailableOnATelcoNetworkProviderResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchDataPlansAvailableOnATelcoNetworkProviderData

class MakeAirtimePurchasesViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str

class MakeAirtimePurchasesViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: MakeAirtimePurchasesViaParentAccountData

class MakeAirtimePurchasesViaSpecificOrSubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str

class MakeAirtimePurchasesViaSpecificOrSubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: MakeAirtimePurchasesViaSpecificOrSubAccountData

class VendDataBundlesViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str

class VendDataBundlesViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendDataBundlesViaParentAccountData

class VendDataBundlesViaSpecificOrSubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str

class VendDataBundlesViaSpecificOrSubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendDataBundlesViaSpecificOrSubAccountData

class CabletvLookupResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class CableTvSubscriptionViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class CableTvSubscriptionViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CableTvSubscriptionViaParentAccountData

class CableTvSubscriptionViaASubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class CableTvSubscriptionViaASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CableTvSubscriptionViaASubAccountData

class FetchElectricityProvidersData(TypedDict, total=False):
    id: str
    name: str

class FetchElectricityProvidersResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchElectricityProvidersData

class ElectricityCustomerLookupResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class VendElectricityViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class VendElectricityViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendElectricityViaParentAccountData

class VendElectricityViaASubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class VendElectricityViaASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendElectricityViaASubAccountData

class FetchBettingProvidersResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class BettingCustomerLookupResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class VendBettingViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class VendBettingViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendBettingViaParentAccountData

class VendBettingViaASubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class VendBettingViaASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendBettingViaASubAccountData

class GetMandatesByFiltersData(TypedDict, total=False):
    items: dict[str, Any]
    page: int
    pageSize: int
    totalItems: int
    totalPages: int
    hasMore: bool

class GetMandatesByFiltersResponse(TypedDict, total=False):
    code: str
    description: str
    data: GetMandatesByFiltersData

class UpdateMandateStatusData(TypedDict, total=False):
    mandateId: str
    mandateStatus: str

class UpdateMandateStatusResponse(TypedDict, total=False):
    code: str
    description: str
    data: UpdateMandateStatusData

class DebitAMandateData(TypedDict, total=False):
    mandateId: str
    status: str
    amount: str
    message: str

class DebitAMandateResponse(TypedDict, total=False):
    code: str
    description: str
    data: DebitAMandateData

class GetMandateStatusData(TypedDict, total=False):
    customerAccountName: str
    mandateId: str
    customerAccountNumber: str
    mandateStatus: str
    rejectionComment: str
    mandateAdviceStatus: str

class GetMandateStatusResponse(TypedDict, total=False):
    code: str
    description: str
    data: GetMandateStatusData

class GetMandateByIdData(TypedDict, total=False):
    status: str
    customerAccountNumber: str
    customerAccountName: str
    bankCode: str
    amount: float
    customerName: str
    customerAddress: str
    customerEmail: str
    customerPhoneNumber: str
    merchantReference: str
    frequency: str
    startDate: list[int]
    endDate: list[int]
    mandateAdviceStatus: str
    mandateId: str

class GetMandateByIdResponse(TypedDict, total=False):
    code: str
    description: str
    data: GetMandateByIdData

class CreateADirectDebitMandateResponse(TypedDict, total=False):
    responseMessage: str
    responseCode: str
    data: dict[str, Any]

class AuthorizeTransferData(TypedDict, total=False):
    wtTransactionId: str
    coreTransactionId: str
    status: str
    coreStatus: str
    type: str
    prettyStatus: str
    meta: dict[str, Any]

class AuthorizeTransferResponse(TypedDict, total=False):
    code: str
    description: str
    data: AuthorizeTransferData

class AuthorizeExchangeData(TypedDict, total=False):
    wtTransactionId: str
    coreTransactionId: str
    status: str
    coreStatus: str
    type: str

class AuthorizeExchangeResponse(TypedDict, total=False):
    code: str
    description: str
    data: AuthorizeExchangeData

class ConvertMoneyData(TypedDict, total=False):
    fromAmount: float
    fromCurrency: str
    fromFormatted: str
    toAmount: float
    toCurrency: str
    toFormatted: str
    spreadAmount: float
    spreadCurrency: str
    exchangeRateId: str
    currencyPairName: str
    feeAmount: float
    feeCurrency: str

class ConvertMoneyResponse(TypedDict, total=False):
    code: str
    description: str
    data: ConvertMoneyData

class FetchExchangeRatesData(TypedDict, total=False):
    rates: list[dict[str, Any]]

class FetchExchangeRatesResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchExchangeRatesData

class FetchGlobalPayoutTransactionData(TypedDict, total=False):
    transactionId: str
    status: str
    coreStatus: str
    type: str
    createdAt: str

class FetchGlobalPayoutTransactionResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchGlobalPayoutTransactionData

class FetchPaymentMethodsResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class ListInstitutionProvidersResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class InitiateMobileMoneyInflowData(TypedDict, total=False):
    transactionReference: str
    status: str
    message: str
    idempotencyKey: str

class InitiateMobileMoneyInflowResponse(TypedDict, total=False):
    code: str
    description: str
    data: InitiateMobileMoneyInflowData

class FetchCollectionTransactionData(TypedDict, total=False):
    transactionId: str
    coreUserId: str
    account: str
    status: str
    amount: float
    currency: str

class FetchCollectionTransactionResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCollectionTransactionData

class CancelCheckoutOrderData(TypedDict, total=False):
    success: bool
    message: str

class CancelCheckoutOrderResponse(TypedDict, total=False):
    code: str
    description: str
    data: CancelCheckoutOrderData

class FetchDrcInflowProvidersResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class FetchDrcInflowProvidersSandboxResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]
