from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_failure import TransferFailure


class SandboxTransferSimulateRequest(BaseModel):
    failure_reason: Optional[TransferFailure] = None
    """The failure reason if the event type for a transfer is `"failed"` or `"returned"`. Null value otherwise."""

    transfer_id: str
    """Plaid’s unique identifier for a transfer."""

    event_type: str
    """The asynchronous event to be simulated. May be: `posted`, `failed`, or `returned`.
    
    An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:
    
    `pending` --> `failed`
    
    `pending` --> `posted`
    
    `posted` --> `returned`
    """

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SandboxTransferSimulateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SandboxTransferSimulateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
