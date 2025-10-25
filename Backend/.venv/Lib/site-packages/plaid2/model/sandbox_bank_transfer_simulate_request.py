from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .bank_transfer_failure import BankTransferFailure


class SandboxBankTransferSimulateRequest(BaseModel):
    event_type: str
    """The asynchronous event to be simulated. May be: `posted`, `failed`, or `reversed`.
    
    An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:
    
    `pending` --> `failed`
    
    `pending` --> `posted`
    
    `posted` --> `reversed`
    """

    failure_reason: Optional[BankTransferFailure] = None
    """The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise."""

    bank_transfer_id: str
    """Plaid’s unique identifier for a bank transfer."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SandboxBankTransferSimulateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SandboxBankTransferSimulateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
