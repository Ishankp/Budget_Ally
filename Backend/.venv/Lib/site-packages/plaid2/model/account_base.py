from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .account_balance import AccountBalance

_ALIAS_MAP = {"name_": "name"}


class AccountBase(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    subtype: Optional[str] = None
    """See the [Account type schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full listing of account types and corresponding subtypes."""

    name_: str
    """The name of the account, either assigned by the user or by the financial institution itself"""

    balances: AccountBalance
    """A set of fields describing the balance for an account. Balance information may be cached unless the balance object was returned by `/accounts/balance/get`."""

    official_name: Optional[str] = None
    """The official name of the account as given by the financial institution"""

    mask: Optional[str] = None
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

    verification_status: Optional[str] = None
    """The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.
    
    `pending_automatic_verification`: The Item is pending automatic verification
    
    `pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the two amounts.
    
    `automatically_verified`: The Item has successfully been automatically verified	
    
    `manually_verified`: The Item has successfully been manually verified
    
    `verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.
    
    `verification_failed`: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.	
    	"""

    account_id: str
    """Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new `account_id` will be assigned to the account.
    
    The `account_id` can also change if the `access_token` is deleted and the same credentials that were used to generate that `access_token` are used to generate a new `access_token` on a later date. In that case, the new `account_id` will be different from the old `account_id`.
    
    If an account with a specific `account_id` disappears instead of changing, the account is likely closed. Closed accounts are not returned by the Plaid API.
    
    Like all Plaid identifiers, the `account_id` is case sensitive."""

    type: str
    """`investment:` Investment account. In API versions 2018-05-22 and earlier, this type is called `brokerage` instead.
    
    `credit:` Credit card
    
    `depository:` Depository account
    
    `loan:` Loan account
    
    `other:` Non-specified account type
    
    See the [Account type schema](https://plaid.com/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "AccountBase":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "AccountBase":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
