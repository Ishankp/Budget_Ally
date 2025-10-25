from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .identity_verification_request_user import IdentityVerificationRequestUser


class IdentityVerificationCreateRequest(BaseModel):
    gave_consent: bool
    """A flag specifying whether the end user has already agreed to a privacy policy specifying that their data will be shared with Plaid for verification purposes.
    
    If `gave_consent` is set to `true`, the `accept_tos` step will be marked as `skipped` and the end user's session will start at the next step requirement."""

    user: IdentityVerificationRequestUser
    """User information collected outside of Link, most likely via your own onboarding process.
    
    Each of the following identity fields are optional:
    
    `email_address`
    
    `phone_number`
    
    `date_of_birth`
    
    `name`
    
    `address`
    
    `id_number`
    Specifically, these fields are optional in that they can either be fully provided (satisfying every required field in their subschema)
    or omitted from the request entirely by not providing the key or value.
    Providing these fields via the API will result in Link skipping the data collection process for the associated user. All verification steps enabled in the associated Identity Verification Template will still be run. Verification steps will either be run immediately, or once the user completes the `accept_tos` step, depending on the value provided to the `gave_consent` field."""

    is_idempotent: Optional[bool] = None
    """An optional flag specifying how you would like Plaid to handle attempts to create an Identity Verification when an Identity Verification already exists for the provided `client_user_id` and `template_id`.
    If idempotency is enabled, Plaid will return the existing Identity Verification. If idempotency is disabled, Plaid will reject the request with a `400 Bad Request` status code if an Identity Verification already exists for the supplied `client_user_id` and `template_id`."""

    is_shareable: bool
    """A flag specifying whether you would like Plaid to expose a shareable URL for the verification being created."""

    template_id: str
    """ID of the associated Identity Verification template."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IdentityVerificationCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IdentityVerificationCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
