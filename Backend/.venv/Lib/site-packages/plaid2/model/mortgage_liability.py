from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .mortgage_interest_rate import MortgageInterestRate
from .mortgage_property_address import MortgagePropertyAddress


class MortgageLiability(BaseModel):
    property_address: MortgagePropertyAddress
    """Object containing fields describing property address."""

    escrow_balance: Optional[float] = None
    """Total amount held in escrow to pay taxes and insurance on behalf of the borrower."""

    has_pmi: Optional[bool] = None
    """Indicates whether the borrower has private mortgage insurance in effect."""

    last_payment_amount: Optional[float] = None
    """The amount of the last payment."""

    loan_term: Optional[str] = None
    """Full duration of mortgage as at origination (e.g. `10 year`)."""

    account_number: str
    """The account number of the loan."""

    next_monthly_payment: Optional[float] = None
    """The amount of the next payment."""

    current_late_fee: Optional[float] = None
    """The current outstanding amount charged for late payment."""

    next_payment_due_date: Optional[str] = None
    """The due date for the next payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    last_payment_date: Optional[str] = None
    """The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    account_id: str
    """The ID of the account that this liability belongs to."""

    ytd_principal_paid: Optional[float] = None
    """The YTD principal paid."""

    maturity_date: Optional[str] = None
    """Original date on which mortgage is due in full. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    loan_type_description: Optional[str] = None
    """Description of the type of loan, for example `conventional`, `fixed`, or `variable`. This field is provided directly from the loan servicer and does not have an enumerated set of possible values."""

    has_prepayment_penalty: Optional[bool] = None
    """Indicates whether the borrower will pay a penalty for early payoff of mortgage."""

    origination_date: Optional[str] = None
    """The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    origination_principal_amount: Optional[float] = None
    """The original principal balance of the mortgage."""

    past_due_amount: Optional[float] = None
    """Amount of loan (principal + interest) past due for payment."""

    interest_rate: MortgageInterestRate
    """Object containing metadata about the interest rate for the mortgage."""

    ytd_interest_paid: Optional[float] = None
    """The year to date (YTD) interest paid."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "MortgageLiability":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "MortgageLiability":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
