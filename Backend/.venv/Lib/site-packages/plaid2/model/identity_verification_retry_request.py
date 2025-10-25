from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .identity_verification_retry_request_steps_object import IdentityVerificationRetryRequestStepsObject


class IdentityVerificationRetryRequest(BaseModel):
    client_user_id: str
    """An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object."""

    steps: Optional[IdentityVerificationRetryRequestStepsObject] = None
    """Instructions for the `custom` retry strategy specifying which steps should be required or skipped.
    
    
    Note:
    
    
    This field must be provided when the retry strategy is `custom` and must be omitted otherwise.
    
    Custom retries override settings in your Plaid Template. For example, if your Plaid Template has `verify_sms` disabled, a custom retry with `verify_sms` enabled will still require the step.
    
    The `selfie_check` step is currently not supported on the sandbox server. Sandbox requests will silently disable the `selfie_check` step when provided."""

    template_id: str
    """ID of the associated Identity Verification template."""

    strategy: str
    """An instruction specifying what steps the new Identity Verification attempt should require the user to complete:
    
    
    `reset` - Restart the user at the beginning of the session, regardless of whether they successfully completed part of their previous session.
    
    `incomplete` - Start the new session at the step that the user failed in the previous session, skipping steps that have already been successfully completed.
    
    `infer` - If the most recent Identity Verification attempt associated with the given `client_user_id` has a status of `failed` or `expired`, retry using the `incomplete` strategy. Otherwise, use the `reset` strategy.
    
    `custom` - Start the new session with a custom configuration, specified by the value of the `steps` field
    
    Note:
    
    The `incomplete` strategy cannot be applied if the session's failing step is `screening` or `risk_check`.
    
    The `infer` strategy cannot be applied if the session's status is still `active`"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IdentityVerificationRetryRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IdentityVerificationRetryRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
