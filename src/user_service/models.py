import enum
import uuid

from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.db import Base


class SocialMediaType(enum.Enum):
    vk = "VK"
    fb = "Facebook"
    inst = "Instagram"
    tg = "Telegram"
    tw = "Twitter"
    wa = "WhatsApp"
    vb = "Viber"


class Roles(enum.Enum):
    photographer = "Photographer"
    customer = "Customer"
    admin = "Admin"


class User(Base):
    __tablename__ = "user"

    id = Column(UUID, default=uuid.uuid4(), primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    phone = Column(String)
    experience = Column(Integer)
    city = Column(String)
    role = Column(Enum(Roles), default=Roles.customer, nullable=False, index=True)
    birthdate = Column(DateTime, nullable=False)
    about = Column(String)

    social_media = relationship("SocialMedia", cascade="all, delete")
    # portfolio = fore
    # genres = fore
    # orders = fore


class SocialMedia(Base):
    __tablename__ = "social media"

    id = Column(UUID, default=uuid.uuid4(), primary_key=True, index=True)
    user_id = Column(UUID, ForeignKey("user.id"), nullable=False)
    link = Column(String, nullable=False)
    type = Column(Enum(SocialMediaType), nullable=False)
