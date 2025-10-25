from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .error import Error


class Item(BaseModel):
    webhook: Optional[str] = None
    """The URL registered to receive webhooks for the Item."""

    item_id: str
    """The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive."""

    update_type: str
    """Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.
    
    `background` - Item can be updated in the background
    
    `user_present_required` - Item requires user interaction to be updated"""

    billed_products: List[str]
    """A list of products that have been billed for the Item. The contents of this array will be mutually exclusive with `available_products`. Note - `billed_products` is populated in all environments but only requests in Production are billed. Also note that products that are billed on a pay-per-call basis rather than a pay-per-Item basis, such as `balance`, will not appear here.
    """

    products: Optional[List[str]] = None
    """A list of authorized products for the Item.
    """

    consented_products: Optional[List[str]] = None
    """Beta: A list of products that have gone through consent collection for the Item. Only present for those enabled in the beta.
    """

    error: Optional[Error] = None
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred."""

    available_products: List[str]
    """A list of products available for the Item that have not yet been accessed. The contents of this array will be mutually exclusive with `billed_products`."""

    consent_expiration_time: Optional[str] = None
    """The RFC 3339 timestamp after which the consent provided by the end user will expire. Upon consent expiration, the item will enter the `ITEM_LOGIN_REQUIRED` error state. To circumvent the `ITEM_LOGIN_REQUIRED` error and maintain continuous consent, the end user can reauthenticate via Link’s update mode in advance of the consent expiration time.
    
    Note - This is only relevant for certain OAuth-based institutions. For all other institutions, this field will be null.
    """

    institution_id: Optional[str] = None
    """The Plaid Institution ID associated with the Item. Field is `null` for Items created via Same Day Micro-deposits."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Item":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Item":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
