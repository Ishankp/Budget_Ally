from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class AssetReportUser(BaseModel):
    last_name: Optional[str] = None
    """The user's last name.  Required for the Fannie Mae Day 1 Certainty™ program."""

    first_name: Optional[str] = None
    """The user's first name. Required for the Fannie Mae Day 1 Certainty™ program."""

    phone_number: Optional[str] = None
    """The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567". Phone numbers provided in other formats will be parsed on a best-effort basis."""

    email: Optional[str] = None
    """The user's email address."""

    middle_name: Optional[str] = None
    """The user's middle name"""

    ssn: Optional[str] = None
    """The user's Social Security Number. Required for the Fannie Mae Day 1 Certainty™ program.
    
    Format: "ddd-dd-dddd" """

    client_user_id: Optional[str] = None
    """An identifier you determine and submit for the user."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "AssetReportUser":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "AssetReportUser":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
