from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .external_payment_initiation_consent_options import ExternalPaymentInitiationConsentOptions
from .payment_initiation_consent_constraints import PaymentInitiationConsentConstraints


class PaymentInitiationConsentCreateRequest(BaseModel):
    constraints: PaymentInitiationConsentConstraints
    """Limitations that will be applied to payments initiated using the payment consent."""

    recipient_id: str
    """The ID of the recipient the payment consent is for. The created consent can be used to transfer funds to this recipient only."""

    reference: str
    """A reference for the payment consent. This must be an alphanumeric string with at most 18 characters and must not contain any special characters."""

    scopes: List[str]
    """An array of payment consent scopes."""

    options: Optional[ExternalPaymentInitiationConsentOptions] = None
    """Additional payment consent options"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationConsentCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationConsentCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
