from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .income_summary_field_number import IncomeSummaryFieldNumber
from .income_summary_field_string import IncomeSummaryFieldString
from .pay_frequency import PayFrequency
from .transaction_data import TransactionData


class IncomeSummary(BaseModel):
    projected_wage: IncomeSummaryFieldNumber
    """The employee's estimated annual salary, as derived from information reported on the paystub."""

    employer_name: IncomeSummaryFieldString
    """The name of the employer, as reported on the paystub."""

    verified_transaction: Optional[TransactionData] = None
    """Information about the matched direct deposit transaction used to verify a user's payroll information."""

    pay_frequency: Optional[PayFrequency] = None
    """The frequency of the pay period."""

    employee_name: IncomeSummaryFieldString
    """The name of the employee, as reported on the paystub."""

    ytd_gross_income: IncomeSummaryFieldNumber
    """Year-to-date pre-tax earnings, as reported on the paystub."""

    ytd_net_income: IncomeSummaryFieldNumber
    """Year-to-date earnings after any tax withholdings, benefit payments or deductions, as reported on the paystub."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IncomeSummary":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IncomeSummary":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
