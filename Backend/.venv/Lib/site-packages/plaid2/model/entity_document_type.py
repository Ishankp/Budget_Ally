from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class EntityDocumentType(str, Enum):
    bik = "bik"
    business_number = "business_number"
    imo = "imo"
    other = "other"
    swift = "swift"
    tax_id = "tax_id"
