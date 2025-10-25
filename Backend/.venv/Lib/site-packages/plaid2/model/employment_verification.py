from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .platform_ids import PlatformIds


class EmploymentVerification(BaseModel):
    platform_ids: Optional[PlatformIds] = None
    """An object containing a set of ids related to an employee"""

    start_date: Optional[str] = None
    """Start of employment in ISO 8601 format (YYYY-MM-DD)."""

    status: Optional[str] = None
    """Current employment status."""

    end_date: Optional[str] = None
    """End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD)."""

    employer: Optional[str] = None
    """An object containing employer data."""

    title: Optional[str] = None
    """Current title of employee."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EmploymentVerification":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "EmploymentVerification":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
