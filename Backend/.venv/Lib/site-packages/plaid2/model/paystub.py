from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .deductions import Deductions
from .earnings import Earnings
from .employee import Employee
from .employment_details import EmploymentDetails
from .income_breakdown import IncomeBreakdown
from .net_pay import NetPay
from .pay_period_details import PayPeriodDetails
from .paystub_details import PaystubDetails
from .paystub_employer import PaystubEmployer
from .paystub_verification import PaystubVerification
from .paystub_ytd_details import PaystubYtdDetails


class Paystub(BaseModel):
    earnings: Earnings
    """An object representing both a breakdown of earnings on a paystub and the total earnings."""

    employment_details: Optional[EmploymentDetails] = None
    """An object representing employment details found on a paystub."""

    employer: PaystubEmployer
    """Information about the employer on the paystub"""

    pay_period_details: PayPeriodDetails
    """Details about the pay period."""

    net_pay: NetPay
    """An object representing information about the net pay amount on the paystub."""

    paystub_details: Optional[PaystubDetails] = None
    """An object representing details that can be found on the paystub."""

    deductions: Deductions
    """An object with the deduction information found on a paystub."""

    income_breakdown: Optional[List[IncomeBreakdown]] = None
    employee: Employee
    """Data about the employee."""

    doc_id: str
    """An identifier of the document referenced by the document metadata."""

    ytd_earnings: Optional[PaystubYtdDetails] = None
    """The amount of income earned year to date, as based on paystub data."""

    verification: Optional[PaystubVerification] = None
    """An object containing details on the paystub's verification status. This object will only be populated if the [`income_verification.access_tokens`](/docs/api/tokens/#link-token-create-request-income-verification-access-tokens) parameter was provided during the `/link/token/create` call or if a problem was detected with the information supplied by the user; otherwise it will be `null`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Paystub":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Paystub":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
