from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class CreditBankIncomeCause(BaseModel):
    error_type: Optional[str] = None
    """A broad categorization of the error. Safe for programmatic use."""

    error_message: Optional[str] = None
    """A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use."""

    item_id: Optional[str] = None
    """The `item_id` of the Item associated with this warning."""

    error_code: Optional[str] = None
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues. Error fields will be `null` if no error has occurred."""

    display_message: Optional[str] = None
    """A user-friendly representation of the error code. null if the error is not related to user action.
    This may change over time and is not safe for programmatic use."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeCause":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeCause":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
