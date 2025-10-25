from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PhoneType(str, Enum):
    phone = "phone"
    fax = "fax"
