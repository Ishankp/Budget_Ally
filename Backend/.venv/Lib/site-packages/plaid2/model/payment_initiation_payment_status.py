from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentInitiationPaymentStatus(str, Enum):
    payment_status_input_needed = "PAYMENT_STATUS_INPUT_NEEDED"
    payment_status_processing = "PAYMENT_STATUS_PROCESSING"
    payment_status_initiated = "PAYMENT_STATUS_INITIATED"
    payment_status_completed = "PAYMENT_STATUS_COMPLETED"
    payment_status_insufficient_funds = "PAYMENT_STATUS_INSUFFICIENT_FUNDS"
    payment_status_failed = "PAYMENT_STATUS_FAILED"
    payment_status_blocked = "PAYMENT_STATUS_BLOCKED"
    payment_status_unknown = "PAYMENT_STATUS_UNKNOWN"
    payment_status_executed = "PAYMENT_STATUS_EXECUTED"
    payment_status_authorising = "PAYMENT_STATUS_AUTHORISING"
    payment_status_cancelled = "PAYMENT_STATUS_CANCELLED"
    payment_status_established = "PAYMENT_STATUS_ESTABLISHED"
    payment_status_rejected = "PAYMENT_STATUS_REJECTED"
