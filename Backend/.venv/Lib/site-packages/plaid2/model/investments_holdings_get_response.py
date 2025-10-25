from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .account_base import AccountBase
from .holding import Holding
from .item import Item
from .security import Security


class InvestmentsHoldingsGetResponse(BaseModel):
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""

    holdings: List[Holding]
    """The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field. """

    securities: List[Security]
    """Objects describing the securities held in the accounts associated with the Item. """

    accounts: List[AccountBase]
    """The accounts associated with the Item"""

    item: Item
    """Metadata about the Item."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InvestmentsHoldingsGetResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "InvestmentsHoldingsGetResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
