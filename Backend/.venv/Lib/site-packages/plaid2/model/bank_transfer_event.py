from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .bank_transfer_failure import BankTransferFailure


class BankTransferEvent(BaseModel):
    origination_account_id: Optional[str] = None
    """The ID of the origination account that this balance belongs to."""

    timestamp: str
    """The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`."""

    account_id: str
    """The account ID associated with the bank transfer."""

    event_type: str
    """The type of event that this bank transfer represents.
    
    `pending`: A new transfer was created; it is in the pending state.
    
    `cancelled`: The transfer was cancelled by the client.
    
    `failed`: The transfer failed, no funds were moved.
    
    `posted`: The transfer has been successfully submitted to the payment network.
    
    `reversed`: A posted transfer was reversed."""

    bank_transfer_id: str
    """Plaid’s unique identifier for a bank transfer."""

    bank_transfer_type: str
    """The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""

    failure_reason: Optional[BankTransferFailure] = None
    """The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise."""

    bank_transfer_amount: str
    """The bank transfer amount."""

    event_id: int
    """Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers."""

    bank_transfer_iso_currency_code: str
    """The currency of the bank transfer amount."""

    direction: Optional[str] = None
    """Indicates the direction of the transfer: `outbound` for API-initiated transfers, or `inbound` for payments received by the FBO account."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "BankTransferEvent":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "BankTransferEvent":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
