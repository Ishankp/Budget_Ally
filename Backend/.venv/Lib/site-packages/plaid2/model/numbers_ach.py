from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class NumbersAch(BaseModel):
    account: str
    """The ACH account number for the account.
    
    Note that when using OAuth with Chase Bank (`ins_56`), Chase will issue "tokenized" routing and account numbers, which are not the user's actual account and routing numbers. These tokenized numbers should work identically to normal account and routing numbers. The digits returned in the `mask` field will continue to reflect the actual account number, rather than the tokenized account number; for this reason, when displaying account numbers to the user to help them identify their account in your UI, always use the `mask` rather than truncating the `account` number. If a user revokes their permissions to your app, the tokenized numbers will continue to work for ACH deposits, but not withdrawals."""

    account_id: str
    """The Plaid account ID associated with the account numbers"""

    routing: str
    """The ACH routing number for the account. If the institution is `ins_56`, this may be a tokenized routing number. For more information, see the description of the `account` field."""

    wire_routing: Optional[str] = None
    """The wire transfer routing number for the account, if available"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "NumbersAch":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "NumbersAch":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
