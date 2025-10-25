from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .numbers_international_iban import NumbersInternationalIban
from .recipient_bacs import RecipientBacs


class WalletNumbers(BaseModel):
    bacs: Optional[RecipientBacs] = None
    """An object containing a BACS account number and sort code. If an IBAN is not provided or if you need to accept domestic GBP-denominated payments, BACS data is required."""

    international: Optional[NumbersInternationalIban] = None
    """Account numbers using the International Bank Account Number and BIC/SWIFT code format."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WalletNumbers":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WalletNumbers":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
