from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .payment_amount import PaymentAmount


class PaymentInitiationConsentPaymentExecuteRequest(BaseModel):
    idempotency_key: str
    """A random key provided by the client, per unique consent payment. Maximum of 128 characters.
    
    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. If a request to execute a consent payment fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single payment is created. If the request was successfully processed, it will prevent any payment that uses the same idempotency key, and was received within 24 hours of the first request, from being processed."""

    consent_id: str
    """The consent ID."""

    amount: PaymentAmount
    """The amount and currency of a payment"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationConsentPaymentExecuteRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationConsentPaymentExecuteRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
