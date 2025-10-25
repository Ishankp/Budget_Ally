from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale
from .transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from .transfer_authorization_proposed_transfer import TransferAuthorizationProposedTransfer


class TransferAuthorization(BaseModel):
    decision_rationale: Optional[TransferAuthorizationDecisionRationale] = None
    """The rationale for Plaid's decision regarding a proposed transfer. It is always set for `declined` decisions, and may or may not be null for `approved` decisions."""

    guarantee_decision: Optional[str] = None
    """Indicates whether the transfer is guaranteed by Plaid (Guaranteed ACH customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details."""

    id: str
    """Plaid’s unique identifier for a transfer authorization."""

    guarantee_decision_rationale: Optional[TransferAuthorizationGuaranteeDecisionRationale] = None
    """The rationale for Plaid's decision to not guarantee a transfer. Will be `null` unless `guarantee_decision` is `NOT_GUARANTEED`."""

    decision: str
    """
    A decision regarding the proposed transfer.
    
    `approved` – The proposed transfer has received the end user's consent and has been approved for processing by Plaid. The `decision_rationale` field is set if Plaid was unable to fetch the account information. You may proceed with the transfer, but further review is recommended (i.e., use Link in update to re-authenticate your user when `decision_rationale.code` is `LOGIN_REQUIRED`). Refer to the `code` field in the `decision_rationale` object for details.
    
    `declined` – Plaid reviewed the proposed transfer and declined processing. Refer to the `code` field in the `decision_rationale` object for details."""

    proposed_transfer: TransferAuthorizationProposedTransfer
    """Details regarding the proposed transfer."""

    created: str
    """The datetime representing when the authorization was created, in the format `2006-01-02T15:04:05Z`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferAuthorization":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferAuthorization":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
