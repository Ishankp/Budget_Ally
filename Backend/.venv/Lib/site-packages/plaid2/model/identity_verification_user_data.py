from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .identity_verification_user_address import IdentityVerificationUserAddress
from .user_id_number import UserIdNumber
from .user_name import UserName

_ALIAS_MAP = {"name_": "name"}


class IdentityVerificationUserData(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    name_: Optional[UserName] = None
    """The full name provided by the user. If the user has not submitted their name, this field will be null. Otherwise, both fields are guaranteed to be filled."""

    address: Optional[IdentityVerificationUserAddress] = None
    """Even if an address has been collected, some fields may be null depending on the region's addressing system. For example: * Addresses from the United Kingdom will not include a region * Addresses from Hong Kong will not include postal code"""

    id_number: Optional[UserIdNumber] = None
    """ID number submitted by the user, currently used only for the Identity Verification product. If the user has not submitted this data yet, this field will be `null`. Otherwise, both fields are guaranteed to be filled."""

    ip_address: Optional[str] = None
    """An IPv4 or IPV6 address."""

    date_of_birth: Optional[str] = None
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    phone_number: Optional[str] = None
    """A phone number in E.164 format."""

    email_address: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IdentityVerificationUserData":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IdentityVerificationUserData":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
