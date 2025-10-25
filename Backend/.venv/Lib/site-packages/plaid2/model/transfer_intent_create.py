from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_metadata import TransferMetadata
from .transfer_user_in_response import TransferUserInResponse


class TransferIntentCreate(BaseModel):
    id: str
    """Plaid's unique identifier for the transfer intent object."""

    ach_class: str
    """Specifies the use case of the transfer. Required for transfers on an ACH network.
    
    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts
    
    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment
    
    `"tel"` - Telephone-Initiated Entry
    
    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet"""

    account_id: Optional[str] = None
    """The Plaid `account_id` for the account that will be debited or credited. Returned only if `account_id` was set on intent creation."""

    created: str
    """The datetime the transfer was created. This will be of the form `2006-01-02T15:04:05Z`."""

    description: str
    """A description for the underlying transfer. Maximum of 8 characters."""

    status: str
    """The status of the transfer intent.
    
    - `PENDING` – The transfer intent is pending.
    - `SUCCEEDED` – The transfer intent was successfully created.
    - `FAILED` – The transfer intent was unable to be created."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00")."""

    origination_account_id: str
    """Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used."""

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    metadata: Optional[TransferMetadata] = None
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    - The JSON values must be Strings (no nested JSON objects allowed)
    - Only ASCII characters may be used
    - Maximum of 50 key/value pairs
    - Maximum key length of 40 characters
    - Maximum value length of 500 characters
    """

    require_guarantee: Optional[bool] = None
    """When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guaranteed ACH customers only)."""

    iso_currency_code: str
    """The currency of the transfer amount, e.g. "USD" """

    mode: str
    """The direction of the flow of transfer funds.
    
    - `PAYMENT` – Transfers funds from an end user's account to your business account.
    
    - `DISBURSEMENT` – Transfers funds from your business account to an end user's account."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferIntentCreate":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferIntentCreate":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
