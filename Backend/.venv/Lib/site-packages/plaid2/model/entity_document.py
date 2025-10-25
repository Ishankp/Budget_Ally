from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class EntityDocument(BaseModel):
    number: str
    """The numeric or alphanumeric identifier associated with this document."""

    type: str
    """The kind of official document represented by this object.
    
    `bik` - Russian bank code
    
    `business_number` - A number that uniquely identifies the business within a category of businesses
    
    `imo` - Number assigned to the entity by the International Maritime Organization
    
    `other` - Any document not covered by other categories
    
    `swift` - Number identifying a bank and branch.
    
    `tax_id` - Identification issued for the purpose of collecting taxes"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EntityDocument":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "EntityDocument":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
