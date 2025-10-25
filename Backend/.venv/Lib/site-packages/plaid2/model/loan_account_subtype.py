from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class LoanAccountSubtype(str, Enum):
    auto = "auto"
    business = "business"
    commercial = "commercial"
    construction = "construction"
    consumer = "consumer"
    home_equity = "home equity"
    loan = "loan"
    mortgage = "mortgage"
    line_of_credit = "line of credit"
    student = "student"
    other = "other"
    all = "all"
