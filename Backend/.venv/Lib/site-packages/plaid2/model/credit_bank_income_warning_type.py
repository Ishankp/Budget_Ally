from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class CreditBankIncomeWarningType(str, Enum):
    bank_income_warning = "BANK_INCOME_WARNING"
