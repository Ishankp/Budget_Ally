from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class DepositSwitchStateUpdateWebhook(BaseModel):
    webhook_code: Optional[str] = None
    """`"SWITCH_STATE_UPDATE"`"""

    state: Optional[str] = None
    """
    The state, or status, of the deposit switch.
    
    `initialized`: The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.
    
    `processing`: The deposit switch request has been submitted and is being processed.
    
    `completed`: The user's employer has fulfilled and completed the deposit switch request.
    
    `error`: There was an error processing the deposit switch request.
    
    For more information, see the [Deposit Switch API reference](/docs/deposit-switch/reference#deposit_switchget)."""

    deposit_switch_id: Optional[str] = None
    """The ID of the deposit switch."""

    webhook_type: Optional[str] = None
    """`"DEPOSIT_SWITCH"`"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DepositSwitchStateUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DepositSwitchStateUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
