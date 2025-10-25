from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_1099_filer import Credit1099Filer
from .credit_1099_payer import Credit1099Payer
from .credit_1099_recipient import Credit1099Recipient
from .credit_document_metadata import CreditDocumentMetadata


class Credit1099(BaseModel):
    payer_state_number: Optional[str] = None
    """Primary state ID."""

    card_not_present_transaction: Optional[float] = None
    """Amount in card not present transactions."""

    crop_insurance_proceeds: Optional[float] = None
    """Amount of crop insurance proceeds."""

    merchant_category_code: Optional[str] = None
    """Merchant category of filer."""

    march_amount: Optional[float] = None
    """Amount reported for March."""

    april_amount: Optional[float] = None
    """Amount reported for April."""

    june_amount: Optional[float] = None
    """Amount reported for June."""

    payer: Optional[Credit1099Payer] = None
    """An object representing a payer used by 1099-MISC tax documents."""

    september_amount: Optional[float] = None
    """Amount reported for September."""

    state_income_lower: Optional[float] = None
    """State income reported for secondary state."""

    february_amount: Optional[float] = None
    """Amount reported for February."""

    november_amount: Optional[float] = None
    """Amount reported for November."""

    document_metadata: Optional[CreditDocumentMetadata] = None
    """Object representing metadata pertaining to the document."""

    filer: Optional[Credit1099Filer] = None
    """An object representing a filer used by 1099-K tax documents."""

    section_409_a_income: Optional[float] = None
    """Amount of 409A income earned by payer."""

    secondary_state_id: Optional[str] = None
    """Secondary state ID."""

    recipient: Optional[Credit1099Recipient] = None
    """An object representing a recipient used in both 1099-K and 1099-MISC tax documents."""

    payer_state_number_lower: Optional[str] = None
    """Secondary state ID."""

    december_amount: Optional[float] = None
    """Amount reported for December."""

    primary_state: Optional[str] = None
    """Primary state of business."""

    fishing_boat_proceeds: Optional[float] = None
    """Amount of fishing boat proceeds from payer."""

    other_income: Optional[float] = None
    """Amount in other income by payer."""

    section_409_a_deferrals: Optional[float] = None
    """Amount of 409A deferrals earned by payer."""

    july_amount: Optional[float] = None
    """Amount reported for July."""

    october_amount: Optional[float] = None
    """Amount reported for October."""

    primary_state_income_tax: Optional[float] = None
    """State income tax reported for primary state."""

    rents: Optional[float] = None
    """Amount in rent by payer."""

    primary_state_id: Optional[str] = None
    """Primary state ID."""

    august_amount: Optional[float] = None
    """Amount reported for August."""

    form_1099_type: Optional[str] = None
    """Form 1099 Type"""

    january_amount: Optional[float] = None
    """Amount reported for January."""

    nonemployee_compensation: Optional[float] = None
    """Amount of nonemployee compensation from payer."""

    gross_amount: Optional[float] = None
    """Gross amount reported."""

    tax_year: Optional[str] = None
    """Tax year of the tax form."""

    state_tax_withheld_lower: Optional[float] = None
    """Amount of state tax withheld of payer for secondary state."""

    secondary_state: Optional[str] = None
    """Secondary state of business."""

    document_id: Optional[str] = None
    """An identifier of the document referenced by the document metadata."""

    state_income: Optional[float] = None
    """State income reported for primary state."""

    gross_proceeds_paid_to_an_attorney: Optional[float] = None
    """Amount of gross proceeds paid to an attorney by payer."""

    royalties: Optional[float] = None
    """Amount in royalties by payer."""

    pse_name: Optional[str] = None
    """Name of the PSE (Payment Settlement Entity)."""

    substitute_payments_in_lieu_of_dividends_or_interest: Optional[float] = None
    """Amount of substitute payments made by payer."""

    pse_telephone_number: Optional[str] = None
    """Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity)."""

    number_of_payment_transactions: Optional[str] = None
    """Number of payment transactions made."""

    may_amount: Optional[float] = None
    """Amount reported for May."""

    medical_and_healthcare_payments: Optional[float] = None
    """Amount of medical and healthcare payments from payer."""

    secondary_state_income_tax: Optional[float] = None
    """State income tax reported for secondary state."""

    payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer: Optional[str] = None
    """Whether or not payer made direct sales over $5000 of consumer products."""

    state_tax_withheld: Optional[float] = None
    """Amount of state tax withheld of payer for primary state."""

    federal_income_tax_withheld: Optional[float] = None
    """Amount of federal income tax withheld from payer."""

    excess_golden_parachute_payments: Optional[float] = None
    """Amount of golden parachute payments made by payer."""

    transactions_reported: Optional[str] = None
    """One of the values will be provided Payment card Third party network"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Credit1099":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Credit1099":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
