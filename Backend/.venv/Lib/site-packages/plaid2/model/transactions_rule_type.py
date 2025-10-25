from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransactionsRuleType(str, Enum):
    exact_match = "EXACT_MATCH"
    substring_match = "SUBSTRING_MATCH"
