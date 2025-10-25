from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .pslf_status import PslfStatus
from .servicer_address_data import ServicerAddressData
from .student_loan_status import StudentLoanStatus
from .student_repayment_plan import StudentRepaymentPlan


class StudentLoan(BaseModel):
    origination_date: Optional[str] = None
    """The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    last_payment_amount: Optional[float] = None
    """The amount of the last payment."""

    outstanding_interest_amount: Optional[float] = None
    """The total dollar amount of the accrued interest balance. For Sallie Mae ( `ins_116944`), this amount is included in the current balance of the loan, so this field will return as `null`."""

    sequence_number: Optional[str] = None
    """The sequence number of the student loan. Heartland ECSI (`ins_116948`) does not make this field available."""

    loan_name: Optional[str] = None
    """The type of loan, e.g., "Consolidation Loans"."""

    minimum_payment_amount: Optional[float] = None
    """The minimum payment due for the next billing cycle. There are some exceptions:
    Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( `ins_116861`), Firstmark (`ins_116295`), Commonbond Firstmark Services (`ins_116950`), Nelnet (`ins_116528`), EdFinancial Services (`ins_116304`), Granite State (`ins_116308`), and Oklahoma Student Loan Authority (`ins_116945`).
    Firstmark (`ins_116295` ) and Navient (`ins_116248`) will display as $0 if there is an autopay program in effect."""

    disbursement_dates: Optional[List[str]] = None
    """The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    expected_payoff_date: Optional[str] = None
    """The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    account_number: Optional[str] = None
    """The account number of the loan. For some institutions, this may be a masked version of the number (e.g., the last 4 digits instead of the entire number)."""

    interest_rate_percentage: float
    """The interest rate on the loan as a percentage."""

    origination_principal_amount: Optional[float] = None
    """The original principal balance of the loan."""

    payment_reference_number: Optional[str] = None
    """The relevant account number that should be used to reference this loan for payments. In the majority of cases, `payment_reference_number` will match a`ccount_number,` but in some institutions, such as Great Lakes (`ins_116861`), it will be different."""

    pslf_status: PslfStatus
    """Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is Fedloan (`ins_116527`). """

    servicer_address: ServicerAddressData
    """The address of the student loan servicer. This is generally the remittance address to which payments should be sent."""

    ytd_principal_paid: Optional[float] = None
    """The year to date (YTD) principal paid. Availability for this field is limited."""

    ytd_interest_paid: Optional[float] = None
    """The year to date (YTD) interest paid. Availability for this field is limited."""

    last_statement_issue_date: Optional[str] = None
    """The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    account_id: Optional[str] = None
    """The ID of the account that this liability belongs to."""

    is_overdue: Optional[bool] = None
    """`true` if a payment is currently overdue. Availability for this field is limited."""

    repayment_plan: StudentRepaymentPlan
    """An object representing the repayment plan for the student loan"""

    guarantor: Optional[str] = None
    """The guarantor of the student loan."""

    last_payment_date: Optional[str] = None
    """The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    loan_status: StudentLoanStatus
    """An object representing the status of the student loan"""

    next_payment_due_date: Optional[str] = None
    """The due date for the next payment. The due date is `null` if a payment is not expected. A payment is not expected if `loan_status.type` is `deferment`, `in_school`, `consolidated`, `paid in full`, or `transferred`. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "StudentLoan":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "StudentLoan":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
