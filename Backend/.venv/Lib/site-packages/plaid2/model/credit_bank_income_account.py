from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .owner import Owner

_ALIAS_MAP = {"name_": "name"}


class CreditBankIncomeAccount(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    owners: Optional[List[Owner]] = None
    mask: Optional[str] = None
    """The last 2-4 alphanumeric characters of an account's official account number.
    Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

    account_id: Optional[str] = None
    """Plaid's unique identifier for the account."""

    subtype: Optional[str] = None
    """Valid account subtypes for depository accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-depository)."""

    name_: Optional[str] = None
    """The name of the bank account."""

    official_name: Optional[str] = None
    """The official name of the bank account."""

    type: Optional[str] = None
    """The account type. This will always be `depository`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeAccount":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeAccount":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
