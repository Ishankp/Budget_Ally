from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_metadata import TransferMetadata
from .transfer_user_in_request import TransferUserInRequest


class TransferCreateRequest(BaseModel):
    origination_account_id: Optional[str] = None
    """Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank."""

    ach_class: str
    """Specifies the use case of the transfer. Required for transfers on an ACH network.
    
    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts
    
    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment
    
    `"tel"` - Telephone-Initiated Entry
    
    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet"""

    network: str
    """The network or rails used for the transfer. Valid options are `ach` or `same-day-ach`. The cutoff for same-day transfers is 7:45 AM Pacific Time and the cutoff for next-day transfers is 5:45 PM Pacific Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable."""

    authorization_id: str
    """Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier."""

    metadata: Optional[TransferMetadata] = None
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    - The JSON values must be Strings (no nested JSON objects allowed)
    - Only ASCII characters may be used
    - Maximum of 50 key/value pairs
    - Maximum key length of 40 characters
    - Maximum value length of 500 characters
    """

    type: str
    """The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""

    access_token: Optional[str] = None
    """The Plaid `access_token` for the account that will be debited or credited."""

    description: str
    """The transfer description. Maximum of 10 characters."""

    idempotency_key: Optional[str] = None
    """Deprecated. `authorization_id` is now used as idempotency instead.
    
    A random key provided by the client, per unique transfer. Maximum of 50 characters.
    
    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single transfer is created."""

    account_id: Optional[str] = None
    """The Plaid `account_id` for the account that will be debited or credited."""

    user: TransferUserInRequest
    """The legal name and other information for the account holder."""

    iso_currency_code: Optional[str] = None
    """The currency of the transfer amount. The default value is "USD"."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00")."""

    payment_profile_id: Optional[str] = None
    """Plaid’s unique identifier for a payment profile."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
