from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class Holding(BaseModel):
    account_id: str
    """The Plaid `account_id` associated with the holding."""

    institution_price_as_of: Optional[str] = None
    """The date at which `institution_price` was current."""

    cost_basis: Optional[float] = None
    """The original total value or the purchase price per share of the holding. This field is an aggregate on a per holding basis and dependent on the information provided by the institution."""

    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
    """

    security_id: str
    """The Plaid `security_id` associated with the holding."""

    institution_price_datetime: Optional[str] = None
    """Date and time at which `institution_price` was current, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).
    
    This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00).
    """

    quantity: float
    """The total quantity of the asset held, as reported by the financial institution. If the security is an option, `quantity` will reflect the total number of options (typically the number of contracts multiplied by 100), not the number of contracts."""

    iso_currency_code: Optional[str] = None
    """The ISO-4217 currency code of the holding. Always `null` if `unofficial_currency_code` is non-`null`."""

    institution_value: float
    """The value of the holding, as reported by the institution."""

    institution_price: float
    """The last price given by the institution for this security."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Holding":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Holding":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
