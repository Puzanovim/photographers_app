from datetime import datetime
from typing import Optional

from ..models import Roles
from ..schemas import UserBase, UserDB, UserCreate


class Photographer(UserBase):
    role: Roles = Roles.photographer
    experience: Optional[int] = 0
    about: Optional[str] = None


class PhotographerDB(Photographer, UserDB):
    pass


class PhotographerCreate(Photographer, UserCreate):
    role: Optional[Roles] = Roles.photographer


class PhotographerUpdate(PhotographerCreate):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    role: Optional[Roles]
    password: Optional[str]
    created_date: Optional[datetime]
