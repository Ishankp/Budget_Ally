from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class AccountSelectionCardinality(str, Enum):
    single_select = "SINGLE_SELECT"
    multi_select = "MULTI_SELECT"
    all = "ALL"
