from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class ExpirationDate(str, Enum):
    not_expired = "not_expired"
    expired = "expired"
    no_data = "no_data"
