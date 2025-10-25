from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class Products(str, Enum):
    assets = "assets"
    auth = "auth"
    balance = "balance"
    identity = "identity"
    investments = "investments"
    liabilities = "liabilities"
    payment_initiation = "payment_initiation"
    identity_verification = "identity_verification"
    transactions = "transactions"
    credit_details = "credit_details"
    income = "income"
    income_verification = "income_verification"
    deposit_switch = "deposit_switch"
    standing_orders = "standing_orders"
    transfer = "transfer"
    employment = "employment"
    recurring_transactions = "recurring_transactions"
