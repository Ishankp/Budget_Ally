from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class RecurringTransactionsUpdateWebhook(BaseModel):
    item_id: str
    """The `item_id` of the Item associated with this webhook, warning, or error"""

    webhook_type: str
    """`TRANSACTIONS`"""

    webhook_code: str
    """`RECURRING_TRANSACTIONS_UPDATE`"""

    account_ids: List[str]
    """A list of `account_ids` for accounts that have new or updated recurring transactions data."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "RecurringTransactionsUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "RecurringTransactionsUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
