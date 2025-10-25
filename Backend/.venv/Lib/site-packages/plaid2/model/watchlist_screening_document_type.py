from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class WatchlistScreeningDocumentType(str, Enum):
    birth_certificate = "birth_certificate"
    drivers_license = "drivers_license"
    immigration_number = "immigration_number"
    military_id = "military_id"
    other = "other"
    passport = "passport"
    personal_identification = "personal_identification"
    ration_card = "ration_card"
    ssn = "ssn"
    student_id = "student_id"
    tax_id = "tax_id"
    travel_document = "travel_document"
    voter_id = "voter_id"
