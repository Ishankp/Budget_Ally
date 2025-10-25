from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .link_token_create_request_income_verification_bank_income import (
    LinkTokenCreateRequestIncomeVerificationBankIncome,
)
from .link_token_create_request_income_verification_payroll_income import (
    LinkTokenCreateRequestIncomeVerificationPayrollIncome,
)
from .link_token_create_request_user_stated_income_source import LinkTokenCreateRequestUserStatedIncomeSource


class LinkTokenCreateRequestIncomeVerification(BaseModel):
    stated_income_sources: Optional[List[LinkTokenCreateRequestUserStatedIncomeSource]] = None
    """A list of user stated income sources"""

    precheck_id: Optional[str] = None
    """The ID of a precheck created with `/income/verification/precheck`. Will be used to improve conversion of the income verification flow by streamlining the Link interface presented to the end user."""

    income_source_types: Optional[List[str]] = None
    """The types of source income data that users will be permitted to share. Options include `bank` and `payroll`. Currently you can only specify one of these options."""

    access_tokens: Optional[List[str]] = None
    """An array of access tokens corresponding to Items that a user has previously connected with. Data from these institutions will be cross-referenced with document data received during the Document Income flow to help verify that the uploaded documents are accurate. If the `transactions` product was not initialized for these Items during link, it will be initialized after this Link session.
    
    This field should only be used with the `payroll` income source type."""

    asset_report_id: Optional[str] = None
    """The `asset_report_id` of an asset report associated with the user, as provided by `/asset_report/create`. Providing an `asset_report_id` is optional and can be used to verify the user through a streamlined flow. If provided, the bank linking flow will be skipped."""

    income_verification_id: Optional[str] = None
    """The `income_verification_id` of the verification instance, as provided by `/income/verification/create`."""

    payroll_income: Optional[LinkTokenCreateRequestIncomeVerificationPayrollIncome] = None
    """Specifies options for initializing Link for use with Payroll Income. This field is required if `income_verification` is included in the `products` array and `payroll` is specified in `income_source_types`."""

    bank_income: Optional[LinkTokenCreateRequestIncomeVerificationBankIncome] = None
    """Specifies options for initializing Link for use with Bank Income. This field is required if `income_verification` is included in the `products` array and `bank` is specified in `income_source_types`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenCreateRequestIncomeVerification":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenCreateRequestIncomeVerification":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
