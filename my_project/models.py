from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)

    prompt = Column(String, nullable=False)

    image_path = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")