from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentConsentPeriodicAlignment(str, Enum):
    calendar = "CALENDAR"
    consent = "CONSENT"
