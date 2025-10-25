from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentInitiationConsentPaymentExecuteResponse(BaseModel):
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""

    payment_id: str
    """A unique ID identifying the payment"""

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

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationConsentPaymentExecuteResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationConsentPaymentExecuteResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
