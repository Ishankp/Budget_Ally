from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class AccountType(str, Enum):
    investment = "investment"
    credit = "credit"
    depository = "depository"
    loan = "loan"
    brokerage = "brokerage"
    other = "other"
