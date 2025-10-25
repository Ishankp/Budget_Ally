from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .bank_transfer_metadata import BankTransferMetadata
from .bank_transfer_user import BankTransferUser


class ProcessorBankTransferCreateRequest(BaseModel):
    processor_token: str
    """The processor token obtained from the Plaid integration partner. Processor tokens are in the format: `processor-<environment>-<identifier>`"""

    metadata: Optional[BankTransferMetadata] = None
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    - The JSON values must be Strings (no nested JSON objects allowed)
    - Only ASCII characters may be used
    - Maximum of 50 key/value pairs
    - Maximum key length of 40 characters
    - Maximum value length of 500 characters
    """

    amount: str
    """The amount of the bank transfer (decimal string with two digits of precision e.g. "10.00")."""

    iso_currency_code: str
    """The currency of the transfer amount – should be set to "USD"."""

    origination_account_id: Optional[str] = None
    """Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified."""

    description: str
    """The transfer description. Maximum of 10 characters."""

    idempotency_key: str
    """A random key provided by the client, per unique bank transfer. Maximum of 50 characters.
    
    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a bank transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single bank transfer is created."""

    user: BankTransferUser
    """The legal name and other information for the account holder."""

    network: str
    """The network or rails used for the transfer. Valid options are `ach`, `same-day-ach`, or `wire`."""

    ach_class: Optional[str] = None
    """Specifies the use case of the transfer. Required for transfers on an ACH network.
    
    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts
    
    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment
    
    `"tel"` - Telephone-Initiated Entry
    
    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet"""

    type: str
    """The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""

    custom_tag: Optional[str] = None
    """An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ProcessorBankTransferCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ProcessorBankTransferCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
