from pydantic import BaseModel
from typing import List, Optional


class Expense(BaseModel):
    id: Optional[int]
    description: str
    category: str
    amount: float
    frequency: str
    priority: int


class UserSettings(BaseModel):
    tax_rate: float
    savings_rate: float
