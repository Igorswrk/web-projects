from pydantic import BaseModel, EmailStr, Field
from uuid import UUID, uuid4
from datetime import date


class Team(BaseModel):
    id: UUID | None = None
    dt_fundation: date
    name: str
    description: str | None = None
    number_of_honours: int 
