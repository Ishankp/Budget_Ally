from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferEventListRequest(BaseModel):
    end_date: Optional[str] = None
    """The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)"""

    sweep_id: Optional[str] = None
    """Plaid’s unique identifier for a sweep."""

    count: Optional[int] = None
    """The maximum number of transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned."""

    event_types: Optional[List[str]] = None
    """Filter events by event type."""

    origination_account_id: Optional[str] = None
    """The origination account ID to get events for transfers from a specific origination account."""

    start_date: Optional[str] = None
    """The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)"""

    transfer_id: Optional[str] = None
    """Plaid’s unique identifier for a transfer."""

    offset: Optional[int] = None
    """The offset into the list of transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned."""

    account_id: Optional[str] = None
    """The account ID to get events for all transactions to/from an account."""

    transfer_type: Optional[str] = None
    """The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into your origination account; a `credit` indicates a transfer of money out of your origination account."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferEventListRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferEventListRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
