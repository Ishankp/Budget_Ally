from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .employee import Employee
from .paystub_employer import PaystubEmployer
from .w_2_box_12 import W2Box12
from .w_2_state_and_local_wages import W2StateAndLocalWages


class W2(BaseModel):
    state_and_local_wages: Optional[List[W2StateAndLocalWages]] = None
    social_security_tips: Optional[str] = None
    """Tips from social security."""

    box_12: Optional[List[W2Box12]] = None
    tax_year: Optional[str] = None
    """The tax year of the W2 document."""

    nonqualified_plans: Optional[str] = None
    """Nonqualified plans."""

    social_security_wages: Optional[str] = None
    """Wages from social security."""

    social_security_tax_withheld: Optional[str] = None
    """Social security tax withheld for the tax year."""

    statutory_employee: Optional[str] = None
    """Statutory employee."""

    employer_id_number: Optional[str] = None
    """An employee identification number or EIN."""

    medicare_wages_and_tips: Optional[str] = None
    """Wages and tips from medicare."""

    employee: Optional[Employee] = None
    """Data about the employee."""

    allocated_tips: Optional[str] = None
    """Allocated tips."""

    retirement_plan: Optional[str] = None
    """Retirement plan."""

    medicare_tax_withheld: Optional[str] = None
    """Medicare tax withheld for the tax year."""

    box_9: Optional[str] = None
    """Contents from box 9 on the W2."""

    dependent_care_benefits: Optional[str] = None
    """Dependent care benefits."""

    wages_tips_other_comp: Optional[str] = None
    """Wages from tips and other compensation."""

    third_party_sick_pay: Optional[str] = None
    """Third party sick pay."""

    employer: Optional[PaystubEmployer] = None
    """Information about the employer on the paystub"""

    federal_income_tax_withheld: Optional[str] = None
    """Federal income tax withheld for the tax year."""

    other: Optional[str] = None
    """Other."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "W2":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "W2":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
