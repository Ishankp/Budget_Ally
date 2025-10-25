from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransactionsGetRequestOptions(BaseModel):
    include_personal_finance_category: Optional[bool] = None
    """Include the [`personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-personal-finance-category) object in the response.
    
    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    
    We’re introducing Category Rules - a new beta endpoint that will enable you to change the `personal_finance_category` for a transaction based on your users’ needs. When rules are set, the selected category will override the Plaid provided category. To learn more, send a note to transactions-feedback@plaid.com."""

    account_ids: Optional[List[str]] = None
    """A list of `account_ids` to retrieve for the Item
    
    Note: An error will be returned if a provided `account_id` is not associated with the Item."""

    include_personal_finance_category_beta: Optional[bool] = None
    """Please use [`include_personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-get-request-options-include-personal-finance-category) instead."""

    offset: Optional[int] = None
    """The number of transactions to skip. The default value is 0."""

    include_original_description: Optional[bool] = None
    """Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager."""

    count: Optional[int] = None
    """The number of transactions to fetch."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionsGetRequestOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransactionsGetRequestOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
