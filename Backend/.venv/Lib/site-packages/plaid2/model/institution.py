from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .auth_supported_methods import AuthSupportedMethods
from .institution_status import InstitutionStatus
from .payment_initiation_metadata import PaymentInitiationMetadata

_ALIAS_MAP = {"name_": "name"}


class Institution(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    institution_id: str
    """Unique identifier for the institution"""

    products: List[str]
    """A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return `auth` in the product array; institutions that do not list `auth` may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those methods, use the `auth_metadata` object. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/)."""

    payment_initiation_metadata: Optional[PaymentInitiationMetadata] = None
    """Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests."""

    country_codes: List[str]
    """A list of the country codes supported by the institution."""

    routing_numbers: List[str]
    """A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution."""

    logo: Optional[str] = None
    """Base64 encoded representation of the institution's logo"""

    url: Optional[str] = None
    """The URL for the institution's website"""

    primary_color: Optional[str] = None
    """Hexadecimal representation of the primary color used by the institution"""

    name_: str
    """The official name of the institution"""

    status: Optional[InstitutionStatus] = None
    """The status of an institution is determined by the health of its Item logins, Transactions updates, Investments updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate data.
    
    Institution status is accessible in the Dashboard and via the API using the `/institutions/get_by_id` endpoint with the `include_status` option set to true. Note that institution status is not available in the Sandbox environment.
    """

    auth_metadata: Optional[AuthSupportedMethods] = None
    """Metadata that captures information about the Auth features of an institution."""

    oauth: bool
    """Indicates that the institution has an OAuth login flow."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Institution":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Institution":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
