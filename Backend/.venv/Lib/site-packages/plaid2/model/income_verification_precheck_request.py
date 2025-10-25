from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .income_verification_precheck_employer import IncomeVerificationPrecheckEmployer
from .income_verification_precheck_military_info import IncomeVerificationPrecheckMilitaryInfo
from .income_verification_precheck_user import IncomeVerificationPrecheckUser


class IncomeVerificationPrecheckRequest(BaseModel):
    employer: Optional[IncomeVerificationPrecheckEmployer] = None
    """Information about the end user's employer"""

    transactions_access_tokens: Optional[List[str]] = None
    """An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note that if the Items specified here are not already initialized with `transactions`, providing them in this field will cause these Items to be initialized with (and billed for) the Transactions product."""

    us_military_info: Optional[IncomeVerificationPrecheckMilitaryInfo] = None
    """Data about military info in the income verification precheck."""

    transactions_access_token: Optional[str] = None
    user: Optional[IncomeVerificationPrecheckUser] = None
    """Information about the user whose eligibility is being evaluated."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IncomeVerificationPrecheckRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IncomeVerificationPrecheckRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
