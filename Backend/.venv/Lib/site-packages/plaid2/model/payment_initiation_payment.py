from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .external_payment_refund_details import ExternalPaymentRefundDetails
from .external_payment_schedule_base import ExternalPaymentScheduleBase
from .payment_amount import PaymentAmount
from .recipient_bacs import RecipientBacs


class PaymentInitiationPayment(BaseModel):
    iban: Optional[str] = None
    """The International Bank Account Number (IBAN) for the sender, if specified in the `/payment_initiation/payment/create` call."""

    status: str
    """The status of the payment.
    
    `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.
    
    `PAYMENT_STATUS_INITIATED`: The payment has been successfully authorised and accepted by the financial institution but has not been executed.
    
    `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.
    
    `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.
    
    `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.
    
    `PAYMENT_STATUS_AUTHORISING`: The payment is currently being processed. The payment will automatically exit this state when the financial institution has authorised the transaction.
    
    `PAYMENT_STATUS_CANCELLED`: The payment was cancelled during authorisation.
    
    `PAYMENT_STATUS_EXECUTED`: The payment has been successfully initiated and is considered complete.
    
    `PAYMENT_STATUS_ESTABLISHED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.
    
    `PAYMENT_STATUS_REJECTED`: The payment was rejected by the financial institution.
    
    Deprecated:
    These statuses will be removed in a future release.
    
    `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.
    
    `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.
    
    `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders."""

    bacs: Optional[RecipientBacs] = None
    """An object containing a BACS account number and sort code. If an IBAN is not provided or if this recipient needs to accept domestic GBP-denominated payments, BACS data is required."""

    adjusted_scheme: Optional[str] = None
    """Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.
    
    `FASTER_PAYMENTS`: Enables payments to move quickly between UK bank accounts. Default value in the UK.
    
    `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.
    
    `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks."""

    last_status_update: str
    """The date and time of the last time the `status` was updated, in IS0 8601 format"""

    schedule: Optional[ExternalPaymentScheduleBase] = None
    """The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up as a standing order. If no schedule is specified, the payment will be executed only once."""

    recipient_id: str
    """The ID of the recipient"""

    payment_id: str
    """The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive."""

    consent_id: Optional[str] = None
    """The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent."""

    adjusted_reference: Optional[str] = None
    """The value of the reference sent to the bank after adjustment to pass bank validation rules."""

    amount: PaymentAmount
    """The amount and currency of a payment"""

    refund_ids: Optional[List[str]] = None
    """Refund IDs associated with the payment."""

    refund_details: Optional[ExternalPaymentRefundDetails] = None
    """Details about external payment refund"""

    wallet_id: Optional[str] = None
    """The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""

    scheme: Optional[str] = None
    """Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.
    
    `FASTER_PAYMENTS`: Enables payments to move quickly between UK bank accounts. Default value in the UK.
    
    `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.
    
    `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks."""

    reference: str
    """A reference for the payment."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationPayment":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationPayment":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
