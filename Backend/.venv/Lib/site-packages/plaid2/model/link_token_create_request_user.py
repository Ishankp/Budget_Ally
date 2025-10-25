from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .user_address import UserAddress
from .user_id_number import UserIdNumber
from .user_name import UserName

_ALIAS_MAP = {"name_": "name"}


class LinkTokenCreateRequestUser(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    name_: Optional[UserName] = None
    """The user's full name. Optional if using the [Identity Verification](https://plaid.com/docs/api/products/identity-verification) product; if not using Identity Verification, this field is not allowed. Users will not be asked for their name when this field is provided."""

    date_of_birth: Optional[str] = None
    """To be provided in the format "yyyy-mm-dd". Not currently used."""

    client_user_id: str
    """A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`. It is currently used as a means of searching logs for the given user in the Plaid Dashboard."""

    address: Optional[UserAddress] = None
    """Home address for the user."""

    phone_number_verified_time: Optional[str] = None
    """The date and time the phone number was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This field is optional, but required to enable any [returning user experience](https://plaid.com/docs/link/returning-user).
    
     Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.
    
     Example: `2020-01-01T00:00:00Z`
    """

    id_number: Optional[UserIdNumber] = None
    """ID number submitted by the user, currently used only for the Identity Verification product. If the user has not submitted this data yet, this field will be `null`. Otherwise, both fields are guaranteed to be filled."""

    legal_name: Optional[str] = None
    """The user's full legal name. Currently used only to support certain legacy flows."""

    email_address_verified_time: Optional[str] = None
    """The date and time the email address was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This is an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user).
    
     Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.
    
     Example: `2020-01-01T00:00:00Z`"""

    phone_number: Optional[str] = None
    """The user's phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. This field is optional, but required to enable the [returning user experience](https://plaid.com/docs/link/returning-user)."""

    ssn: Optional[str] = None
    """To be provided in the format "ddd-dd-dddd". Not currently used."""

    email_address: Optional[str] = None
    """The user's email address. This field is optional, but required to enable the [pre-authenticated returning user flow](https://plaid.com/docs/link/returning-user/#enabling-the-returning-user-experience)."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenCreateRequestUser":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenCreateRequestUser":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
