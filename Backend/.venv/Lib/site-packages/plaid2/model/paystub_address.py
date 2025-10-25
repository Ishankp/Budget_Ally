from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaystubAddress(BaseModel):
    line_2: Optional[str] = None
    """Street address line 2."""

    region: Optional[str] = None
    """The region or state
    Example: `"NC"`"""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    city: Optional[str] = None
    """The full city name."""

    street: Optional[str] = None
    """The full street address."""

    line_1: Optional[str] = None
    """Street address line 1."""

    country: Optional[str] = None
    """The ISO 3166-1 alpha-2 country code."""

    state_code: Optional[str] = None
    """The region or state
    Example: `"NC"`"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaystubAddress":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaystubAddress":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
