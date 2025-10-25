from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IdentityVerificationStepSummary(BaseModel):
    watchlist_screening: str
    """The status of a step in the identity verification process."""

    risk_check: str
    """The status of a step in the identity verification process."""

    selfie_check: str
    """The status of a step in the identity verification process."""

    kyc_check: str
    """The status of a step in the identity verification process."""

    verify_sms: str
    """The status of a step in the identity verification process."""

    accept_tos: str
    """The status of a step in the identity verification process."""

    documentary_verification: str
    """The status of a step in the identity verification process."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IdentityVerificationStepSummary":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IdentityVerificationStepSummary":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
