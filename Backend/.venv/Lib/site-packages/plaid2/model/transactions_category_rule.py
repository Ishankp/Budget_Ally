from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transactions_rule_details import TransactionsRuleDetails


class TransactionsCategoryRule(BaseModel):
    item_id: Optional[str] = None
    """A unique identifier of the item the rule was created for"""

    created_at: Optional[str] = None
    """Date and time when a rule was created in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ).
    """

    personal_finance_category: Optional[str] = None
    """Personal finance category unique identifier.
    
    In the personal finance category taxonomy, this field is represented by the detailed category field.
    """

    id: Optional[str] = None
    """A unique identifier of the rule created"""

    rule_details: Optional[TransactionsRuleDetails] = None
    """A representation of transactions rule details."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionsCategoryRule":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransactionsCategoryRule":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
