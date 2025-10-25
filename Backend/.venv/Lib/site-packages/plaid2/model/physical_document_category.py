from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PhysicalDocumentCategory(str, Enum):
    drivers_license = "drivers_license"
    id_card = "id_card"
    passport = "passport"
    residence_permit_card = "residence_permit_card"
    resident_card = "resident_card"
