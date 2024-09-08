from typing import Optional

from pydantic import BaseModel


class CreateLinkRequest(BaseModel):
    name: str
    hex_color: str
