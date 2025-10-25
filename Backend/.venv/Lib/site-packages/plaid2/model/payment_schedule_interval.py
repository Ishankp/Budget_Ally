from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentScheduleInterval(str, Enum):
    weekly = "WEEKLY"
    monthly = "MONTHLY"
