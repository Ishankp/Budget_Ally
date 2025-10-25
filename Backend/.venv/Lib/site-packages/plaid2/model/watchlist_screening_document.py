from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class WatchlistScreeningDocument(BaseModel):
    type: str
    """The kind of official document represented by this object.
    
    `birth_certificate` - A certificate of birth
    
    `drivers_license` - A license to operate a motor vehicle
    
    `immigration_number` - Immigration or residence documents
    
    `military_id` - Identification issued by a military group
    
    `other` - Any document not covered by other categories
    
    `passport` - An official passport issue by a government
    
    `personal_identification` - Any generic personal identification that is not covered by other categories
    
    `ration_card` - Identification that entitles the holder to rations
    
    `ssn` - United States Social Security Number
    
    `student_id` - Identification issued by an educational institution
    
    `tax_id` - Identification issued for the purpose of collecting taxes
    
    `travel_document` - Visas, entry permits, refugee documents, etc.
    
    `voter_id` - Identification issued for the purpose of voting"""

    number: str
    """The numeric or alphanumeric identifier associated with this document."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WatchlistScreeningDocument":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WatchlistScreeningDocument":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
