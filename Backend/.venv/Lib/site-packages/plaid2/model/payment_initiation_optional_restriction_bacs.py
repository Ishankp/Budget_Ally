from typing import Any, Dict, Optional, Union
from pydantic import BaseModel
from .recipient_bacs import RecipientBacs


class PaymentInitiationOptionalRestrictionBacs(BaseModel):
    recipient_bacs: Optional[RecipientBacs] = None
    """An object containing a BACS account number and sort code. If an IBAN is not provided or if you need to accept
    domestic GBP-denominated payments, BACS data is required."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationOptionalRestrictionBacs":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationOptionalRestrictionBacs":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
