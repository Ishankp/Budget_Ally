from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class WalletListRequest(BaseModel):
    cursor: Optional[str] = None
    """A base64 value representing the latest e-wallet that has already been requested. Set this to `next_cursor` received from the previous `/wallet/list` request. If provided, the response will only contain e-wallets created before that e-wallet. If omitted, the response will contain e-wallets starting from the most recent, and in descending order."""

    count: Optional[int] = None
    """The number of e-wallets to fetch"""

    iso_currency_code: Optional[str] = None
    """An ISO-4217 currency code, used with e-wallets and transactions."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WalletListRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WalletListRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
