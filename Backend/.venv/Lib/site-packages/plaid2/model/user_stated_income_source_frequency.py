from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class UserStatedIncomeSourceFrequency(str, Enum):
    unknown = "UNKNOWN"
    weekly = "WEEKLY"
    biweekly = "BIWEEKLY"
    semi_monthly = "SEMI_MONTHLY"
    monthly = "MONTHLY"
