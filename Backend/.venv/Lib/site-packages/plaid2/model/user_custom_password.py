from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .mfa import Mfa
from .override_accounts import OverrideAccounts


class UserCustomPassword(BaseModel):
    mfa: Mfa
    """Specifies the multi-factor authentication settings to use with this test account"""

    override_accounts: List[OverrideAccounts]
    """An array of account overrides to configure the accounts for the Item. By default, if no override is specified, transactions and account data will be randomly generated based on the account type and subtype, and other products will have fixed or empty data."""

    force_error: str
    """An error code to force on Item creation. Possible values are:
    
    `"INSTITUTION_NOT_RESPONDING"`
    `"INSTITUTION_NO_LONGER_SUPPORTED"`
    `"INVALID_CREDENTIALS"`
    `"INVALID_MFA"`
    `"ITEM_LOCKED"`
    `"ITEM_LOGIN_REQUIRED"`
    `"ITEM_NOT_SUPPORTED"`
    `"INVALID_LINK_TOKEN"`
    `"MFA_NOT_SUPPORTED"`
    `"NO_ACCOUNTS"`
    `"PLAID_ERROR"`
    `"USER_SETUP_REQUIRED"`"""

    version: Optional[str] = None
    """The version of the password schema to use, possible values are 1 or 2. The default value is 2. You should only specify 1 if you know it is necessary for your test suite."""

    recaptcha: str
    """You may trigger a reCAPTCHA in Plaid Link in the Sandbox environment by using the recaptcha field. Possible values are `good` or `bad`. A value of `good` will result in successful Item creation and `bad` will result in a `RECAPTCHA_BAD` error to simulate a failed reCAPTCHA. Both values require the reCAPTCHA to be manually solved within Plaid Link."""

    seed: str
    """A seed, in the form of a string, that will be used to randomly generate account and transaction data, if this data is not specified using the `override_accounts` argument. If no seed is specified, the randomly generated data will be different each time.
    
    Note that transactions data is generated relative to the Item's creation date. Different Items created on different dates with the same seed for transactions data will have different dates for the transactions. The number of days between each transaction and the Item creation will remain constant. For example, an Item created on December 15 might show a transaction on December 14. An Item created on December 20, using the same seed, would show that same transaction occurring on December 19."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "UserCustomPassword":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "UserCustomPassword":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
