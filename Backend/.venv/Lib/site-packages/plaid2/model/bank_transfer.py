from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .bank_transfer_failure import BankTransferFailure
from .bank_transfer_metadata import BankTransferMetadata
from .bank_transfer_user import BankTransferUser


class BankTransfer(BaseModel):
    metadata: Optional[BankTransferMetadata] = None
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    - The JSON values must be Strings (no nested JSON objects allowed)
    - Only ASCII characters may be used
    - Maximum of 50 key/value pairs
    - Maximum key length of 40 characters
    - Maximum value length of 500 characters
    """

    origination_account_id: str
    """Plaid’s unique identifier for the origination account that was used for this transfer."""

    amount: str
    """The amount of the bank transfer (decimal string with two digits of precision e.g. "10.00")."""

    ach_class: str
    """Specifies the use case of the transfer. Required for transfers on an ACH network.
    
    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts
    
    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment
    
    `"tel"` - Telephone-Initiated Entry
    
    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet"""

    direction: Optional[str] = None
    """Indicates the direction of the transfer: `outbound` for API-initiated transfers, or `inbound` for payments received by the FBO account."""

    created: str
    """The datetime when this bank transfer was created. This will be of the form `2006-01-02T15:04:05Z`"""

    cancellable: bool
    """When `true`, you can still cancel this bank transfer."""

    network: str
    """The network or rails used for the transfer. Valid options are `ach`, `same-day-ach`, or `wire`."""

    iso_currency_code: str
    """The currency of the transfer amount, e.g. "USD" """

    status: str
    """The status of the transfer."""

    type: str
    """The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""

    account_id: str
    """The account ID that should be credited/debited for this bank transfer."""

    description: str
    """The description of the transfer."""

    failure_reason: Optional[BankTransferFailure] = None
    """The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise."""

    custom_tag: Optional[str] = None
    """A string containing the custom tag provided by the client in the create request. Will be null if not provided."""

    id: str
    """Plaid’s unique identifier for a bank transfer."""

    user: BankTransferUser
    """The legal name and other information for the account holder."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "BankTransfer":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "BankTransfer":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
