from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IncomeVerificationPrecheckConfidence(str, Enum):
    high = "HIGH"
    low = "LOW"
    unknown = "UNKNOWN"
