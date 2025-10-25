from typing import Any, Dict, Optional, Union
from pydantic import BaseModel
from .error import Error


class PlaidError(BaseModel):
    error: Optional[Error] = None
    """We use standard HTTP response codes for success and failure notifications, and our errors are further
    classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or
    user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has
    occurred."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PlaidError":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PlaidError":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
