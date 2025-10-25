from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .error import Error


class PaymentStatusUpdateWebhook(BaseModel):
    original_reference: Optional[str] = None
    """The original value of the reference when creating the payment."""

    adjusted_reference: Optional[str] = None
    """The value of the reference sent to the bank after adjustment to pass bank validation rules."""

    original_start_date: Optional[str] = None
    """The original value of the `start_date` provided during the creation of a standing order. If the payment is not a standing order, this field will be `null`."""

    adjusted_start_date: Optional[str] = None
    """The start date sent to the bank after adjusting for holidays or weekends.  Will be provided in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). If the start date did not require adjustment, or if the payment is not a standing order, this field will be `null`."""

    webhook_type: str
    """`PAYMENT_INITIATION`"""

    webhook_code: str
    """`PAYMENT_STATUS_UPDATE`"""

    payment_id: str
    """The `payment_id` for the payment being updated"""

    timestamp: str
    """The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. `"2017-09-14T14:42:19.350Z"`"""

    error: Optional[Error] = None
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred."""

    new_payment_status: str
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

    old_payment_status: str
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
    def parse_obj(cls, data: Any) -> "PaymentStatusUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentStatusUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
