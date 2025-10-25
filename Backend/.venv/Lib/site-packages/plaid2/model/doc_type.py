from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class DocType(str, Enum):
    unknown = "UNKNOWN"
    document_type_paystub = "DOCUMENT_TYPE_PAYSTUB"
    document_type_bank_statement = "DOCUMENT_TYPE_BANK_STATEMENT"
    document_type_us_tax_w_2 = "DOCUMENT_TYPE_US_TAX_W2"
    document_type_us_military_eras = "DOCUMENT_TYPE_US_MILITARY_ERAS"
    document_type_us_military_les = "DOCUMENT_TYPE_US_MILITARY_LES"
    document_type_us_military_cles = "DOCUMENT_TYPE_US_MILITARY_CLES"
    document_type_gig = "DOCUMENT_TYPE_GIG"
    document_type_none = "DOCUMENT_TYPE_NONE"
    document_type_us_tax_1099_misc = "DOCUMENT_TYPE_US_TAX_1099_MISC"
    document_type_us_tax_1099_k = "DOCUMENT_TYPE_US_TAX_1099_K"
