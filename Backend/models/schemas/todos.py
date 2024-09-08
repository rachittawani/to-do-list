from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class ToDoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    list_details_uuid: Optional[str] = None
    due_date: date
    complete: bool


class ToDoResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    complete: bool
