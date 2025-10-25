from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class OverrideAccountType(str, Enum):
    investment = "investment"
    credit = "credit"
    depository = "depository"
    loan = "loan"
    payroll = "payroll"
    other = "other"
