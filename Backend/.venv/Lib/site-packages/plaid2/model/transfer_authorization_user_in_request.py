from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_user_address_in_request import TransferUserAddressInRequest


class TransferAuthorizationUserInRequest(BaseModel):
    address: Optional[TransferUserAddressInRequest] = None
    """The address associated with the account holder. Providing this data will improve the likelihood that Plaid will be able to guarantee the transfer, if applicable."""

    legal_name: str
    """The user's legal name."""

    email_address: Optional[str] = None
    """The user's email address. In order to qualify for a guaranteed transfer, at least one of `phone_number` or `email_address` must be provided."""

    phone_number: Optional[str] = None
    """The user's phone number. In order to qualify for a guaranteed transfer, at least one of `phone_number` or `email_address` must be provided."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferAuthorizationUserInRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferAuthorizationUserInRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
