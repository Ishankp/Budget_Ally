from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale
from .transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from .transfer_intent_get_failure_reason import TransferIntentGetFailureReason
from .transfer_metadata import TransferMetadata
from .transfer_user_in_response import TransferUserInResponse


class TransferIntentGet(BaseModel):
    failure_reason: Optional[TransferIntentGetFailureReason] = None
    """The reason for a failed transfer intent. Returned only if the transfer intent status is `failed`. Null otherwise."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00")."""

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    iso_currency_code: str
    """The currency of the transfer amount, e.g. "USD" """

    require_guarantee: Optional[bool] = None
    """When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guaranteed ACH customers only)."""

    guarantee_decision_rationale: Optional[TransferAuthorizationGuaranteeDecisionRationale] = None
    """The rationale for Plaid's decision to not guarantee a transfer. Will be `null` unless `guarantee_decision` is `NOT_GUARANTEED`."""

    origination_account_id: str
    """Plaid’s unique identifier for the origination account used for the transfer."""

    guarantee_decision: Optional[str] = None
    """Indicates whether the transfer is guaranteed by Plaid (Guaranteed ACH customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details."""

    created: str
    """The datetime the transfer was created. This will be of the form `2006-01-02T15:04:05Z`."""

    authorization_decision: Optional[str] = None
    """
    A decision regarding the proposed transfer.
    
    `APPROVED` – The proposed transfer has received the end user's consent and has been approved for processing by Plaid. The `decision_rationale` field is set if Plaid was unable to fetch the account information. You may proceed with the transfer, but further review is recommended (i.e., use Link in update to re-authenticate your user when `decision_rationale.code` is `LOGIN_REQUIRED`). Refer to the `code` field in the `decision_rationale` object for details.
    
    `DECLINED` – Plaid reviewed the proposed transfer and declined processing. Refer to the `code` field in the `decision_rationale` object for details."""

    mode: str
    """The direction of the flow of transfer funds.
    
    - `PAYMENT` – Transfers funds from an end user's account to your business account.
    
    - `DISBURSEMENT` – Transfers funds from your business account to an end user's account."""

    status: str
    """The status of the transfer intent.
    
    - `PENDING` – The transfer intent is pending.
    - `SUCCEEDED` – The transfer intent was successfully created.
    - `FAILED` – The transfer intent was unable to be created."""

    authorization_decision_rationale: Optional[TransferAuthorizationDecisionRationale] = None
    """The rationale for Plaid's decision regarding a proposed transfer. It is always set for `declined` decisions, and may or may not be null for `approved` decisions."""

    description: str
    """A description for the underlying transfer. Maximum of 8 characters."""

    metadata: Optional[TransferMetadata] = None
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    - The JSON values must be Strings (no nested JSON objects allowed)
    - Only ASCII characters may be used
    - Maximum of 50 key/value pairs
    - Maximum key length of 40 characters
    - Maximum value length of 500 characters
    """

    transfer_id: Optional[str] = None
    """Plaid's unique identifier for the transfer created through the UI. Returned only if the transfer was successfully created. Null value otherwise."""

    account_id: Optional[str] = None
    """The Plaid `account_id` for the account that will be debited or credited. Returned only if `account_id` was set on intent creation."""

    id: str
    """Plaid's unique identifier for a transfer intent object."""

    ach_class: str
    """Specifies the use case of the transfer. Required for transfers on an ACH network.
    
    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts
    
    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment
    
    `"tel"` - Telephone-Initiated Entry
    
    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferIntentGet":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferIntentGet":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
