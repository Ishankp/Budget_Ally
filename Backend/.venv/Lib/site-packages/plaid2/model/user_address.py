from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class UserAddress(BaseModel):
    street: str
    """The primary street portion of an address. If the user has submitted their address, this field will always be filled."""

    city: str
    """City from the end user's address"""

    country: str
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form."""

    region: str
    """An ISO 3166-2 subdivision code. Related terms would be "state", "province", "prefecture", "zone", "subdivision", etc."""

    street_2: Optional[str] = None
    """Extra street information, like an apartment or suite number."""

    postal_code: str
    """The postal code for the associated address. Between 2 and 10 alphanumeric characters."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "UserAddress":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "UserAddress":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
