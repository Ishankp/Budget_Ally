from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferUserAddressInRequest(BaseModel):
    postal_code: Optional[str] = None
    """The postal code (e.g., "94103")."""

    region: Optional[str] = None
    """The state or province (e.g., "CA")."""

    country: Optional[str] = None
    """A two-letter country code (e.g., "US")."""

    street: Optional[str] = None
    """The street number and name (i.e., "100 Market St.")."""

    city: Optional[str] = None
    """Ex. "San Francisco" """

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferUserAddressInRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferUserAddressInRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
