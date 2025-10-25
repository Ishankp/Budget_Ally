from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class SignalPersonName(BaseModel):
    suffix: Optional[str] = None
    """The user's name suffix (e.g. "II")"""

    family_name: Optional[str] = None
    """The user's family name / surname"""

    prefix: Optional[str] = None
    """The user's name prefix (e.g. "Mr.")"""

    given_name: Optional[str] = None
    """The user's given name. If the user has a one-word name, it should be provided in this field."""

    middle_name: Optional[str] = None
    """The user's middle name"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SignalPersonName":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SignalPersonName":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
