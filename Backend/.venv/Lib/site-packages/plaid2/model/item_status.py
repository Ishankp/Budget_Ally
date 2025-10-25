from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .item_status_investments import ItemStatusInvestments
from .item_status_last_webhook import ItemStatusLastWebhook
from .item_status_transactions import ItemStatusTransactions


class ItemStatus(BaseModel):
    transactions: Optional[ItemStatusTransactions] = None
    """Information about the last successful and failed transactions update for the Item."""

    investments: Optional[ItemStatusInvestments] = None
    """Information about the last successful and failed investments update for the Item."""

    last_webhook: Optional[ItemStatusLastWebhook] = None
    """Information about the last webhook fired for the Item."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ItemStatus":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ItemStatus":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
