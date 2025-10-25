from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class WalletTransactionsListRequest(BaseModel):
    cursor: Optional[str] = None
    """A base64 value representing the latest transaction that has already been requested. Set this to `next_cursor` received from the previous `/wallet/transactions/list` request. If provided, the response will only contain transactions created before that transaction. If omitted, the response will contain transactions starting from the most recent, and in descending order by the `created_at` time."""

    count: Optional[int] = None
    """The number of transactions to fetch"""

    wallet_id: str
    """The ID of the e-wallet to fetch transactions from"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WalletTransactionsListRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WalletTransactionsListRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
