from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class CreditBankIncomeCategory(str, Enum):
    salary = "SALARY"
    unemployment = "UNEMPLOYMENT"
    cash = "CASH"
    gig_economy = "GIG_ECONOMY"
    rental = "RENTAL"
    child_support = "CHILD_SUPPORT"
    military = "MILITARY"
    retirement = "RETIREMENT"
    long_term_disability = "LONG_TERM_DISABILITY"
    bank_interest = "BANK_INTEREST"
    other = "OTHER"
