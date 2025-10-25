from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class EarningsBreakdownCanonicalDescription(str, Enum):
    bonus = "BONUS"
    commission = "COMMISSION"
    overtime = "OVERTIME"
    paid_time_off = "PAID TIME OFF"
    regular_pay = "REGULAR PAY"
    vacation = "VACATION"
    basic_allowance_housing = "BASIC ALLOWANCE HOUSING"
    basic_allowance_subsistence = "BASIC ALLOWANCE SUBSISTENCE"
    other = "OTHER"
