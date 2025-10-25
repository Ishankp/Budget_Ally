from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentInitiationRefundStatus(str, Enum):
    processing = "PROCESSING"
    executed = "EXECUTED"
    initiated = "INITIATED"
    failed = "FAILED"
