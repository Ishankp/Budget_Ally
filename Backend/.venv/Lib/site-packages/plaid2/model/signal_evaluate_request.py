from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .signal_device import SignalDevice
from .signal_user import SignalUser


class SignalEvaluateRequest(BaseModel):
    access_token: str
    """The access token associated with the Item data is being requested for."""

    device: Optional[SignalDevice] = None
    """Details about the end user's device"""

    amount: float
    """The transaction amount, in USD (e.g. `102.05`)"""

    client_user_id: Optional[str] = None
    """A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. The max length for this field is 36 characters."""

    account_id: str
    """The `account_id` of the account whose verification status is to be modified"""

    user_present: Optional[bool] = None
    """`true` if the end user is present while initiating the ACH transfer and the endpoint is being called; `false` otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing)."""

    client_transaction_id: str
    """The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters."""

    user: Optional[SignalUser] = None
    """Details about the end user initiating the transaction (i.e., the account holder)."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SignalEvaluateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SignalEvaluateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
