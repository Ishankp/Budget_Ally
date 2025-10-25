from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .address import Address
from .pslf_status import PslfStatus
from .student_loan_repayment_model import StudentLoanRepaymentModel
from .student_loan_status import StudentLoanStatus


class LiabilityOverride(BaseModel):
    origination_date: str
    """The date on which the loan was initially lent, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Can only be set if `type` is `student`."""

    loan_name: str
    """Override the `loan_name` field. Can only be set if `type` is `student`."""

    cash_apr: float
    """The cash APR percentage value. Can only be set if `type` is `credit`."""

    interest_capitalization_grace_period_months: float
    """If set, interest capitalization begins at the given number of months after loan origination. By default interest is never capitalized. Can only be set if `type` is `student`."""

    last_payment_amount: float
    """Override the `last_payment_amount` field. Can only be set if `type` is `credit`."""

    pslf_status: PslfStatus
    """Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is Fedloan (`ins_116527`). """

    nominal_apr: float
    """The interest rate on the loan as a percentage. Can only be set if `type` is `student`."""

    expected_payoff_date: str
    """Override the `expected_payoff_date` field. Can only be set if `type` is `student`."""

    purchase_apr: float
    """The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest charges. Can only be set if `type` is `credit`."""

    is_overdue: bool
    """Override the `is_overdue` field"""

    servicer_address: Address
    """A physical mailing address."""

    type: str
    """The type of the liability object, either `credit` or `student`. Mortgages are not currently supported in the custom Sandbox."""

    minimum_payment_amount: float
    """Override the `minimum_payment_amount` field. Can only be set if `type` is `credit` or `student`."""

    principal: float
    """The original loan principal. Can only be set if `type` is `student`."""

    payment_reference_number: str
    """Override the `payment_reference_number` field. Can only be set if `type` is `student`."""

    repayment_plan_description: str
    """Override the `repayment_plan.description` field. Can only be set if `type` is `student`."""

    repayment_model: StudentLoanRepaymentModel
    """Student loan repayment information used to configure Sandbox test data for the Liabilities product"""

    special_apr: float
    """The special APR percentage value. Can only be set if `type` is `credit`."""

    sequence_number: str
    """Override the `sequence_number` field. Can only be set if `type` is `student`."""

    balance_transfer_apr: float
    """The balance transfer APR percentage value. Can only be set if `type` is `credit`. Can only be set if `type` is `credit`."""

    is_federal: bool
    """Override the `is_federal` field. Can only be set if `type` is `student`."""

    guarantor: str
    """Override the `guarantor` field. Can only be set if `type` is `student`."""

    loan_status: StudentLoanStatus
    """An object representing the status of the student loan"""

    repayment_plan_type: str
    """Override the `repayment_plan.type` field. Can only be set if `type` is `student`. Possible values are: `"extended graduated"`, `"extended standard"`, `"graduated"`, `"income-contingent repayment"`, `"income-based repayment"`, `"interest only"`, `"other"`, `"pay as you earn"`, `"revised pay as you earn"`, or `"standard"`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LiabilityOverride":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LiabilityOverride":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
