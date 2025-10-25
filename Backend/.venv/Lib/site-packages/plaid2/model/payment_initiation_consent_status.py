from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentInitiationConsentStatus(str, Enum):
    unauthorised = "UNAUTHORISED"
    authorised = "AUTHORISED"
    revoked = "REVOKED"
    rejected = "REJECTED"
    expired = "EXPIRED"
