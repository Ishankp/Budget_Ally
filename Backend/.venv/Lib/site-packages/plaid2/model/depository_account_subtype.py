from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class DepositoryAccountSubtype(str, Enum):
    checking = "checking"
    savings = "savings"
    hsa = "hsa"
    cd = "cd"
    money_market = "money market"
    paypal = "paypal"
    prepaid = "prepaid"
    cash_management = "cash management"
    ebt = "ebt"
    all = "all"
