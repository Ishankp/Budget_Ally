from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaystubVerificationStatus(str, Enum):
    paystub_verification_status_unknown = "PAYSTUB_VERIFICATION_STATUS_UNKNOWN"
    paystub_verification_status_verified = "PAYSTUB_VERIFICATION_STATUS_VERIFIED"
    paystub_verification_status_fraudulent = "PAYSTUB_VERIFICATION_STATUS_FRAUDULENT"
