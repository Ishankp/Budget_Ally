from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class SignalEvaluateCoreAttributes(BaseModel):
    p_50_credit_transactions_amount_28_d: Optional[float] = None
    """The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited"""

    plaid_non_oauth_authentication_attempts_count_30_d: Optional[int] = None
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days"""

    phone_change_count_90_d: Optional[int] = None
    """The number of times the account's phone numbers on file have changed over the past 90 days"""

    current_balance: Optional[float] = None
    """Current balance, as of the `balance_last_updated` time. The current balance is the total amount of funds in the account."""

    total_debit_transactions_amount_10_d: Optional[float] = None
    """The total debit (outflow) transaction amount over the past 10 days from the account that will be debited"""

    address_change_count_90_d: Optional[int] = None
    """The number of times the account's addresses on file have changed over the past 90 days"""

    days_with_negative_balance_count_90_d: Optional[int] = None
    """The number of days within the past 90 days when the account that will be debited had a negative end-of-day available balance"""

    p_90_eod_balance_60_d: Optional[float] = None
    """The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be debited"""

    p_90_eod_balance_90_d: Optional[float] = None
    """The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be debited"""

    nsf_overdraft_transactions_count_30_d: Optional[int] = None
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited."""

    plaid_connections_count_30_d: Optional[int] = None
    """The number of times the Item has been connected to applications via Plaid over the past 30 days"""

    available_balance: Optional[float] = None
    """Available balance, as of the `balance_last_updated` time. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account."""

    balance_last_updated: Optional[str] = None
    """Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the balance for the given account has been updated."""

    failed_plaid_non_oauth_authentication_attempts_count_30_d: Optional[int] = None
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days"""

    total_debit_transactions_amount_60_d: Optional[float] = None
    """The total debit (outflow) transaction amount over the past 60 days from the account that will be debited"""

    total_credit_transactions_amount_90_d: Optional[float] = None
    """The total credit (inflow) transaction amount over the past 90 days from the account that will be debited"""

    p_50_eod_balance_30_d: Optional[float] = None
    """The 50th percentile of the end-of-day available balance over the past 30 days of the account that will be debited"""

    p_10_eod_balance_31_d_to_60_d: Optional[float] = None
    """The 10th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited"""

    credit_transactions_count_60_d: Optional[int] = None
    """The total number of credit (inflow) transactions over the past 60 days from the account that will be debited"""

    nsf_overdraft_transactions_count_90_d: Optional[int] = None
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited."""

    days_since_first_plaid_connection: Optional[int] = None
    """The number of days since the first time the Item was connected to an application via Plaid"""

    unauthorized_transactions_count_60_d: Optional[int] = None
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited."""

    email_change_count_90_d: Optional[int] = None
    """The number of times the account's email addresses on file have changed over the past 90 days"""

    address_change_count_28_d: Optional[int] = None
    """The number of times the account's addresses on file have changed over the past 28 days"""

    p_95_credit_transactions_amount_28_d: Optional[float] = None
    """The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited"""

    p_50_eod_balance_31_d_to_60_d: Optional[float] = None
    """The 50th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited"""

    debit_transactions_count_60_d: Optional[int] = None
    """The total number of debit (outflow) transactions over the past 60 days from the account that will be debited"""

    email_change_count_28_d: Optional[int] = None
    """The number of times the account's email addresses on file have changed over the past 28 days"""

    unauthorized_transactions_count_90_d: Optional[int] = None
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited."""

    is_savings_or_money_market_account: Optional[bool] = None
    """Indicates if the ACH transaction funding account is a savings/money market account"""

    total_debit_transactions_amount_90_d: Optional[float] = None
    """The total debit (outflow) transaction amount over the past 90 days from the account that will be debited"""

    total_credit_transactions_amount_10_d: Optional[float] = None
    """The total credit (inflow) transaction amount over the past 10 days from the account that will be debited"""

    debit_transactions_count_10_d: Optional[int] = None
    """The total number of debit (outflow) transactions over the past 10 days from the account that will be debited"""

    total_debit_transactions_amount_30_d: Optional[float] = None
    """The total debit (outflow) transaction amount over the past 30 days from the account that will be debited"""

    unauthorized_transactions_count_7_d: Optional[int] = None
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited."""

    p_50_debit_transactions_amount_28_d: Optional[float] = None
    """The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited"""

    p_10_eod_balance_90_d: Optional[float] = None
    """The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be debited"""

    p_50_eod_balance_61_d_to_90_d: Optional[float] = None
    """The 50th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited"""

    unauthorized_transactions_count_30_d: Optional[int] = None
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited."""

    plaid_non_oauth_authentication_attempts_count_7_d: Optional[int] = None
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days"""

    p_10_eod_balance_61_d_to_90_d: Optional[float] = None
    """The 10th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited"""

    debit_transactions_count_30_d: Optional[int] = None
    """The total number of debit (outflow) transactions over the past 30 days from the account that will be debited"""

    p_90_eod_balance_31_d_to_60_d: Optional[float] = None
    """The 90th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the account that will be debited"""

    p_95_debit_transactions_amount_28_d: Optional[float] = None
    """The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited"""

    p_90_eod_balance_30_d: Optional[float] = None
    """The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be debited"""

    phone_change_count_28_d: Optional[int] = None
    """The number of times the account's phone numbers on file have changed over the past 28 days"""

    p_10_eod_balance_60_d: Optional[float] = None
    """The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be debited"""

    plaid_connections_count_7_d: Optional[int] = None
    """The number of times the Item has been connected to applications via Plaid over the past 7 days"""

    credit_transactions_count_90_d: Optional[int] = None
    """The total number of credit (inflow) transactions over the past 90 days from the account that will be debited"""

    nsf_overdraft_transactions_count_7_d: Optional[int] = None
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited."""

    failed_plaid_non_oauth_authentication_attempts_count_3_d: Optional[int] = None
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days"""

    p_50_eod_balance_60_d: Optional[float] = None
    """The 50th percentile of the end-of-day available balance over the past 60 days of the account that will be debited"""

    total_plaid_connections_count: Optional[int] = None
    """The total number of times the Item has been connected to applications via Plaid"""

    failed_plaid_non_oauth_authentication_attempts_count_7_d: Optional[int] = None
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days"""

    debit_transactions_count_90_d: Optional[int] = None
    """The total number of debit (outflow) transactions over the past 90 days from the account that will be debited"""

    p_10_eod_balance_30_d: Optional[float] = None
    """The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be debited"""

    total_credit_transactions_amount_60_d: Optional[float] = None
    """The total credit (inflow) transaction amount over the past 60 days from the account that will be debited"""

    credit_transactions_count_10_d: Optional[int] = None
    """The total number of credit (inflow) transactions over the past 10 days from the account that will be debited"""

    total_credit_transactions_amount_30_d: Optional[float] = None
    """The total credit (inflow) transaction amount over the past 30 days from the account that will be debited"""

    nsf_overdraft_transactions_count_60_d: Optional[int] = None
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited."""

    credit_transactions_count_30_d: Optional[int] = None
    """The total number of credit (inflow) transactions over the past 30 days from the account that will be debited"""

    p_50_eod_balance_90_d: Optional[float] = None
    """The 50th percentile of the end-of-day available balance over the past 90 days of the account that will be debited"""

    p_90_eod_balance_61_d_to_90_d: Optional[float] = None
    """The 90th percentile of the end-of-day available balance between day 61 and day 90 over the past 60 days of the account that will be debited"""

    plaid_non_oauth_authentication_attempts_count_3_d: Optional[int] = None
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SignalEvaluateCoreAttributes":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SignalEvaluateCoreAttributes":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
