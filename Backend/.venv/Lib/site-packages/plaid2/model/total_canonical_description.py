from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TotalCanonicalDescription(str, Enum):
    bonus = "BONUS"
    commission = "COMMISSION"
    overtime = "OVERTIME"
    paid_time_off = "PAID TIME OFF"
    regular_pay = "REGULAR PAY"
    vacation = "VACATION"
    employee_medicare = "EMPLOYEE MEDICARE"
    fica = "FICA"
    social_security_employee_tax = "SOCIAL SECURITY EMPLOYEE TAX"
    medical = "MEDICAL"
    vision = "VISION"
    dental = "DENTAL"
    net_pay = "NET PAY"
    taxes = "TAXES"
    not_found = "NOT_FOUND"
    other = "OTHER"
