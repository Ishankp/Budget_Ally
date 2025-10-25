from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_document_metadata import CreditDocumentMetadata
from .credit_pay_stub_employee import CreditPayStubEmployee
from .credit_pay_stub_employer import CreditPayStubEmployer
from .w_2_box_12 import W2Box12
from .w_2_state_and_local_wages import W2StateAndLocalWages


class CreditW2(BaseModel):
    employee: CreditPayStubEmployee
    """Data about the employee."""

    federal_income_tax_withheld: Optional[str] = None
    """Federal income tax withheld for the tax year."""

    retirement_plan: Optional[str] = None
    """Retirement plan."""

    employer: CreditPayStubEmployer
    """Information about the employer on the pay stub."""

    medicare_wages_and_tips: Optional[str] = None
    """Wages and tips from medicare."""

    dependent_care_benefits: Optional[str] = None
    """Dependent care benefits."""

    social_security_wages: Optional[str] = None
    """Wages from social security."""

    document_id: str
    """An identifier of the document referenced by the document metadata."""

    wages_tips_other_comp: Optional[str] = None
    """Wages from tips and other compensation."""

    box_9: Optional[str] = None
    """Contents from box 9 on the W2."""

    nonqualified_plans: Optional[str] = None
    """Nonqualified plans."""

    document_metadata: CreditDocumentMetadata
    """Object representing metadata pertaining to the document."""

    allocated_tips: Optional[str] = None
    """Allocated tips."""

    other: Optional[str] = None
    """Other."""

    state_and_local_wages: List[W2StateAndLocalWages]
    box_12: List[W2Box12]
    social_security_tax_withheld: Optional[str] = None
    """Social security tax withheld for the tax year."""

    medicare_tax_withheld: Optional[str] = None
    """Medicare tax withheld for the tax year."""

    third_party_sick_pay: Optional[str] = None
    """Third party sick pay."""

    tax_year: Optional[str] = None
    """The tax year of the W2 document."""

    employer_id_number: Optional[str] = None
    """An employee identification number or EIN."""

    social_security_tips: Optional[str] = None
    """Tips from social security."""

    statutory_employee: Optional[str] = None
    """Statutory employee."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditW2":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditW2":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
