from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .numbers_ach import NumbersAch
from .numbers_bacs import NumbersBacs
from .numbers_eft import NumbersEft
from .numbers_international import NumbersInternational


class AuthGetNumbers(BaseModel):
    eft: List[NumbersEft]
    """An array of EFT numbers identifying accounts."""

    bacs: List[NumbersBacs]
    """An array of BACS numbers identifying accounts."""

    ach: List[NumbersAch]
    """An array of ACH numbers identifying accounts."""

    international: List[NumbersInternational]
    """An array of IBAN numbers identifying accounts."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "AuthGetNumbers":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "AuthGetNumbers":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
