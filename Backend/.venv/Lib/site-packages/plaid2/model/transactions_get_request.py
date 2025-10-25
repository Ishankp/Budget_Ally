from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transactions_get_request_options import TransactionsGetRequestOptions


class TransactionsGetRequest(BaseModel):
    start_date: str
    """The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD."""

    options: Optional[TransactionsGetRequestOptions] = None
    """An optional object to be used with the request. If specified, `options` must not be `null`."""

    access_token: str
    """The access token associated with the Item data is being requested for."""

    end_date: str
    """The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionsGetRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransactionsGetRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
