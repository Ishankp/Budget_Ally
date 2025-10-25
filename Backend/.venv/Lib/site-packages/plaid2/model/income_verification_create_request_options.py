from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel


class IncomeVerificationCreateRequestOptions(BaseModel):
    access_tokens: Optional[List[str]] = None
    """An array of access tokens corresponding to the Items that will be cross-referenced with the product data.
    Plaid will attempt to correlate transaction history from these Items with data from the user's paystub, such as
    date and amount. The `verification` status of the paystub as returned by `/income/verification/paystubs/get` will
    indicate if the verification status was successful, or, if not, why it failed. If the `transactions` product was not
    initialized for the Items during Link, it will be initialized after this Link session."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IncomeVerificationCreateRequestOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IncomeVerificationCreateRequestOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
