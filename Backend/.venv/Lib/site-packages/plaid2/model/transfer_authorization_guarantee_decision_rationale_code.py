from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferAuthorizationGuaranteeDecisionRationaleCode(str, Enum):
    return_bank = "RETURN_BANK"
    return_customer = "RETURN_CUSTOMER"
    guarantee_limit_reached = "GUARANTEE_LIMIT_REACHED"
    risk_estimate_unavailable = "RISK_ESTIMATE_UNAVAILABLE"
    required_param_missing = "REQUIRED_PARAM_MISSING"
