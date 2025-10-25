from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentScheme(str, Enum):
    faster_payments = "FASTER_PAYMENTS"
    sepa_credit_transfer = "SEPA_CREDIT_TRANSFER"
    sepa_credit_transfer_instant = "SEPA_CREDIT_TRANSFER_INSTANT"
