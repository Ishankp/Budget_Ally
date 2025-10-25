from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentMeta(BaseModel):
    payment_method: Optional[str] = None
    """The type of transfer, e.g. 'ACH'"""

    reason: Optional[str] = None
    """The payer-supplied description of the transfer."""

    payer: Optional[str] = None
    """For transfers, the party that is paying the transaction."""

    by_order_of: Optional[str] = None
    """The party initiating a wire transfer. Will be `null` if the transaction is not a wire transfer."""

    payee: Optional[str] = None
    """For transfers, the party that is receiving the transaction."""

    ppd_id: Optional[str] = None
    """The ACH PPD ID for the payer."""

    payment_processor: Optional[str] = None
    """The name of the payment processor"""

    reference_number: Optional[str] = None
    """The transaction reference number supplied by the financial institution."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentMeta":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentMeta":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
