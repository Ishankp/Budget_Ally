from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentInitiationPaymentCreateStatus(str, Enum):
    payment_status_input_needed = "PAYMENT_STATUS_INPUT_NEEDED"
