from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class InstitutionsGetRequestOptions(BaseModel):
    products: Optional[List[str]] = None
    """Filter the Institutions based on which products they support. """

    include_optional_metadata: Optional[bool] = None
    """When `true`, return the institution's homepage URL, logo and primary brand color.
    
    Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos."""

    oauth: Optional[bool] = None
    """Limit results to institutions with or without OAuth login flows."""

    include_auth_metadata: Optional[bool] = None
    """When `true`, returns metadata related to the Auth product indicating which auth methods are supported."""

    include_payment_initiation_metadata: Optional[bool] = None
    """When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported."""

    routing_numbers: Optional[List[str]] = None
    """Specify an array of routing numbers to filter institutions. The response will only return institutions that match all of the routing numbers in the array. Routing number records used for this matching are not comprehensive; failure to match a given routing number to an institution does not mean that the institution is unsupported by Plaid."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InstitutionsGetRequestOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "InstitutionsGetRequestOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
