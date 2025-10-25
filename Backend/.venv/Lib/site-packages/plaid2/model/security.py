from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field

_ALIAS_MAP = {"name_": "name"}


class Security(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    cusip: Optional[str] = None
    """9-character CUSIP, an identifier assigned to North American securities."""

    name_: Optional[str] = None
    """A descriptive name for the security, suitable for display."""

    institution_security_id: Optional[str] = None
    """An identifier given to the security by the institution"""

    type: Optional[str] = None
    """The security type of the holding. Valid security types are:
    
    `cash`: Cash, currency, and money market funds
    
    `cryptocurrency`: Digital or virtual currencies
    
    `derivative`: Options, warrants, and other derivative instruments
    
    `equity`: Domestic and foreign equities
    
    `etf`: Multi-asset exchange-traded investment funds
    
    `fixed income`: Bonds and certificates of deposit (CDs)
    
    `loan`: Loans and loan receivables
    
    `mutual fund`: Open- and closed-end vehicles pooling funds of multiple investors
    
    `other`: Unknown or other investment types"""

    close_price_as_of: Optional[str] = None
    """Date for which `close_price` is accurate. Always `null` if `close_price` is `null`."""

    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the security. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s."""

    sedol: Optional[str] = None
    """7-character SEDOL, an identifier assigned to securities in the UK."""

    institution_id: Optional[str] = None
    """If `institution_security_id` is present, this field indicates the Plaid `institution_id` of the institution to whom the identifier belongs."""

    security_id: str
    """A unique, Plaid-specific identifier for the security, used to associate securities with holdings. Like all Plaid identifiers, the `security_id` is case sensitive."""

    ticker_symbol: Optional[str] = None
    """The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available."""

    close_price: Optional[float] = None
    """Price of the security at the close of the previous trading session. Null for non-public securities. 
    
    If the security is a foreign currency this field will be updated daily and will be priced in USD. 
    
    If the security is a cryptocurrency, this field will be updated multiple times a day. As crypto prices can fluctuate quickly and data may become stale sooner than other asset classes, please refer to update_datetime with the time when the price was last updated.
    """

    proxy_security_id: Optional[str] = None
    """In certain cases, Plaid will provide the ID of another security whose performance resembles this security, typically when the original security has low volume, or when a private security can be modeled with a publicly traded security."""

    update_datetime: Optional[str] = None
    """Date and time at which close_price is accurate, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ). Always null if close_price is null."""

    isin: Optional[str] = None
    """12-character ISIN, a globally unique securities identifier."""

    iso_currency_code: Optional[str] = None
    """The ISO-4217 currency code of the price given. Always `null` if `unofficial_currency_code` is non-`null`."""

    is_cash_equivalent: Optional[bool] = None
    """Indicates that a security is a highly liquid asset and can be treated like cash."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Security":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Security":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
