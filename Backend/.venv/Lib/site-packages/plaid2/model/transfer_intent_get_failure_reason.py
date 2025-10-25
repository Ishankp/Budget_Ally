from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferIntentGetFailureReason(BaseModel):
    error_message: Optional[str] = None
    """A human-readable description of the code associated with a failed transfer intent."""

    error_type: Optional[str] = None
    """A broad categorization of the error."""

    error_code: Optional[str] = None
    """A code representing the reason for a failed transfer intent (i.e., an API error or the authorization being declined).
    
    For a full listing of bank transfer errors, see [Bank Transfers errors](https://plaid.com/docs/errors/bank-transfers/)."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferIntentGetFailureReason":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferIntentGetFailureReason":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
