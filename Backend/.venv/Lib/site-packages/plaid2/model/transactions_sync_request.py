from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transactions_sync_request_options import TransactionsSyncRequestOptions


class TransactionsSyncRequest(BaseModel):
    options: Optional[TransactionsSyncRequestOptions] = None
    """An optional object to be used with the request. If specified, `options` must not be `null`."""

    cursor: Optional[str] = None
    """The cursor value represents the last update requested. Providing it will cause the response to only return changes after this update.
    If omitted, the entire history of updates will be returned, starting with the first-added transactions on the item.
    Note: The upper-bound length of this cursor is 256 characters of base64."""

    count: Optional[int] = None
    """The number of transaction updates to fetch."""

    access_token: str
    """The access token associated with the Item data is being requested for."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionsSyncRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransactionsSyncRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
