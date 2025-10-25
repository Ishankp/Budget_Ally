from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .payment_initiation_address import PaymentInitiationAddress
from .recipient_bacs import RecipientBacs

_ALIAS_MAP = {"name_": "name"}


class PaymentInitiationRecipientCreateRequest(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    iban: Optional[str] = None
    """The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is required."""

    bacs: Optional[RecipientBacs] = None
    """An object containing a BACS account number and sort code. If an IBAN is not provided or if this recipient needs to accept domestic GBP-denominated payments, BACS data is required."""

    name_: str
    """The name of the recipient. We recommend using strings of length 18 or less and avoid special characters to ensure compatibility with all institutions."""

    address: Optional[PaymentInitiationAddress] = None
    """The optional address of the payment recipient."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationRecipientCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationRecipientCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
