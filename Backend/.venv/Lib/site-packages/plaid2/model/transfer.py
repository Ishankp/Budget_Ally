from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from .transfer_failure import TransferFailure
from .transfer_metadata import TransferMetadata
from .transfer_user_in_response import TransferUserInResponse


class Transfer(BaseModel):
    cancellable: bool
    """When `true`, you can still cancel this transfer."""

    guarantee_decision: Optional[str] = None
    """Indicates whether the transfer is guaranteed by Plaid (Guaranteed ACH customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details."""

    failure_reason: Optional[TransferFailure] = None
    """The failure reason if the event type for a transfer is `"failed"` or `"returned"`. Null value otherwise."""

    iso_currency_code: str
    """The currency of the transfer amount, e.g. "USD" """

    network: str
    """The network or rails used for the transfer. Valid options are `ach` or `same-day-ach`. The cutoff for same-day transfers is 7:45 AM Pacific Time and the cutoff for next-day transfers is 5:45 PM Pacific Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable."""

    ach_class: str
    """Specifies the use case of the transfer. Required for transfers on an ACH network.
    
    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts
    
    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment
    
    `"tel"` - Telephone-Initiated Entry
    
    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet"""

    status: str
    """The status of the transfer."""

    account_id: str
    """The account ID that should be credited/debited for this transfer."""

    description: str
    """The description of the transfer."""

    id: str
    """Plaid’s unique identifier for a transfer."""

    origination_account_id: str
    """Plaid’s unique identifier for the origination account that was used for this transfer."""

    created: str
    """The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`"""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00")."""

    guarantee_decision_rationale: Optional[TransferAuthorizationGuaranteeDecisionRationale] = None
    """The rationale for Plaid's decision to not guarantee a transfer. Will be `null` unless `guarantee_decision` is `NOT_GUARANTEED`."""

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    sweep_status: Optional[str] = None
    """The status of the sweep for the transfer.
    `unswept`: The transfer hasn't been swept yet.
    `swept`: The transfer was swept to the sweep account.
    `return_swept`: The transfer was returned, funds were pulled back or pushed back to the sweep account.
    `null`: The transfer will never be swept (e.g. if the transfer is cancelled or returned before being swept)"""

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

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Transfer":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Transfer":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
