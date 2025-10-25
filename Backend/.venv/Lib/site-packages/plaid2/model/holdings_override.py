from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .security_override import SecurityOverride


class HoldingsOverride(BaseModel):
    institution_price_as_of: Optional[str] = None
    """The date at which `institution_price` was current. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date."""

    cost_basis: Optional[float] = None
    """The average original value of the holding. Multiple cost basis values for the same security purchased at different prices are not supported."""

    security: SecurityOverride
    """Specify the security associated with the holding or investment transaction. When inputting custom security data to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a security identifier (`ticker_symbol`, `cusip`, `isin`, or `sedol`) are required."""

    currency: str
    """Either a valid `iso_currency_code` or `unofficial_currency_code`"""

    quantity: float
    """The total quantity of the asset held, as reported by the financial institution."""

    institution_price: float
    """The last price given by the institution for this security"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "HoldingsOverride":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "HoldingsOverride":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
