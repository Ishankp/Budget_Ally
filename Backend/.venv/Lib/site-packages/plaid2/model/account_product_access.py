from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class AccountProductAccess(BaseModel):
    account_data: Optional[bool] = None
    """Allow the application to access account data. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    statements: Optional[bool] = None
    """Allow the application to access bank statements. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    tax_documents: Optional[bool] = None
    """Allow the application to access tax documents. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "AccountProductAccess":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "AccountProductAccess":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
