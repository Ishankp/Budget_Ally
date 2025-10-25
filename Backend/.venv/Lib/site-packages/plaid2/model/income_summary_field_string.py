from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IncomeSummaryFieldString(BaseModel):
    value: str
    """The value of the field."""

    verification_status: str
    """The verification status. One of the following:
    
    `"VERIFIED"`: The information was successfully verified.
    
    `"UNVERIFIED"`: The verification has not yet been performed.
    
    `"NEEDS_INFO"`: The verification was attempted but could not be completed due to missing information.
    
    "`UNABLE_TO_VERIFY`": The verification was performed and the information could not be verified.
    
    `"UNKNOWN"`: The verification status is unknown."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IncomeSummaryFieldString":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IncomeSummaryFieldString":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
