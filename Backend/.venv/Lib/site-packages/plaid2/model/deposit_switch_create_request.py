from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .deposit_switch_create_request_options import DepositSwitchCreateRequestOptions


class DepositSwitchCreateRequest(BaseModel):
    target_account_id: str
    """Plaid Account ID that specifies the target bank account. This account will become the recipient for a user's direct deposit."""

    options: Optional[DepositSwitchCreateRequestOptions] = None
    """Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`."""

    country_code: Optional[str] = None
    """ISO-3166-1 alpha-2 country code standard."""

    target_access_token: str
    """Access token for the target Item, typically provided in the Import Item response. """

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DepositSwitchCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DepositSwitchCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
