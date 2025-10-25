from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .documentary_verification import DocumentaryVerification
from .identity_verification_step_summary import IdentityVerificationStepSummary
from .identity_verification_template_reference import IdentityVerificationTemplateReference
from .identity_verification_user_data import IdentityVerificationUserData
from .kyc_check_details import KycCheckDetails


class IdentityVerificationResponse(BaseModel):
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""

    user: IdentityVerificationUserData
    """The identity data that was either collected from the user or provided via API in order to perform an identity verification."""

    template: IdentityVerificationTemplateReference
    """The resource ID and version number of the template configuring the behavior of a given identity verification."""

    id: str
    """ID of the associated Identity Verification attempt."""

    previous_attempt_id: Optional[str] = None
    """The ID for the Identity Verification preceding this session. This field will only be filled if the current Identity Verification is a retry of a previous attempt."""

    status: str
    """The status of this Identity Verification attempt.
    
    
    `active` - The Identity Verification attempt is incomplete. The user may have completed part of the session, but has neither failed or passed.
    
    `success` - The Identity Verification attempt has completed, passing all steps defined to the associated Identity Verification template
    
    `failed` - The user failed one or more steps in the session and was told to contact support.
    
    `expired` - The Identity Verification attempt was active for more than 48 hours without being completed and was automatically marked as expired.
    
    `canceled` - The Identity Verification attempt was canceled, either via the dashboard by a user, or via API. The user may have completed part of the session, but has neither failed or passed.
    
    `pending_review` - The Identity Verification attempt template was configured to perform a screening that had one or more hits needing review."""

    steps: IdentityVerificationStepSummary
    """Each step will be one of the following values:
    
    
    `active` - This step is the user's current step. They are either in the process of completing this step, or they recently closed their Identity Verification attempt while in the middle of this step. Only one step will be marked as `active` at any given point.
    
    `success` - The Identity Verification attempt has completed this step.
    
    `failed` - The user failed this step. This can either call the user to fail the session as a whole, or cause them to fallback to another step depending on how the Identity Verification template is configured. A failed step does not imply a failed session.
    
    `waiting_for_prerequisite` - The user needs to complete another step first, before they progress to this step. This step may never run, depending on if the user fails an earlier step or if the step is only run as a fallback.
    
    `not_applicable` - This step will not be run for this session.
    
    `skipped` - The retry instructions that created this Identity Verification attempt specified that this step should be skipped.
    
    `expired` - This step had not yet been completed when the Identity Verification attempt as a whole expired.
    
    `canceled` - The Identity Verification attempt was canceled before the user completed this step.
    
    `pending_review` - The Identity Verification attempt template was configured to perform a screening that had one or more hits needing review.
    
    `manually_approved` - The step was manually overridden to pass by a team member in the dashboard.
    
    `manually_rejected` - The step was manually overridden to fail by a team member in the dashboard."""

    documentary_verification: Optional[DocumentaryVerification] = None
    """data, images, analysis, and results from the `documentary_verification` step."""

    shareable_url: Optional[str] = None
    """A shareable URL that can be sent directly to the user to complete verification"""

    watchlist_screening_id: Optional[str] = None
    completed_at: Optional[str] = None
    """An ISO8601 formatted timestamp."""

    created_at: str
    """An ISO8601 formatted timestamp."""

    kyc_check: Optional[KycCheckDetails] = None
    """The outcome of the `kyc_check` step."""

    client_user_id: str
    """An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IdentityVerificationResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IdentityVerificationResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
