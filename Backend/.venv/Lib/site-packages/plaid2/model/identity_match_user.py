from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .address_data import AddressData


class IdentityMatchUser(BaseModel):
    phone_number: Optional[str] = None
    """The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567". Phone numbers provided in other formats will be parsed on a best-effort basis."""

    address: Optional[AddressData] = None
    """Data about the components comprising an address."""

    legal_name: Optional[str] = None
    """The user's full legal name."""

    email_address: Optional[str] = None
    """The user's email address."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IdentityMatchUser":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IdentityMatchUser":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
