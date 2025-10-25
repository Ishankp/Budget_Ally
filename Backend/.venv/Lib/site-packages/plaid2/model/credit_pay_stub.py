from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_document_metadata import CreditDocumentMetadata
from .credit_pay_stub_deductions import CreditPayStubDeductions
from .credit_pay_stub_earnings import CreditPayStubEarnings
from .credit_pay_stub_employee import CreditPayStubEmployee
from .credit_pay_stub_employer import CreditPayStubEmployer
from .credit_pay_stub_net_pay import CreditPayStubNetPay
from .credit_pay_stub_verification import CreditPayStubVerification
from .pay_stub_pay_period_details import PayStubPayPeriodDetails


class CreditPayStub(BaseModel):
    employee: CreditPayStubEmployee
    """Data about the employee."""

    deductions: CreditPayStubDeductions
    """An object with the deduction information found on a pay stub."""

    employer: CreditPayStubEmployer
    """Information about the employer on the pay stub."""

    document_id: Optional[str] = None
    """An identifier of the document referenced by the document metadata."""

    document_metadata: CreditDocumentMetadata
    """Object representing metadata pertaining to the document."""

    pay_period_details: PayStubPayPeriodDetails
    """Details about the pay period."""

    net_pay: CreditPayStubNetPay
    """An object representing information about the net pay amount on the pay stub."""

    verification: Optional[CreditPayStubVerification] = None
    """(To be deprecated) Verification info will be moved to a separate endpoint in the future. An object containing details on the paystub's verification status. This object will only be populated if the [`income_verification.access_tokens`](/docs/api/tokens/#link-token-create-request-income-verification-access-tokens) parameter was provided during the `/link/token/create` call or if a problem was detected with the information supplied by the user; otherwise it will be `null`."""

    earnings: CreditPayStubEarnings
    """An object representing both a breakdown of earnings on a pay stub and the total earnings."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditPayStub":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditPayStub":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
