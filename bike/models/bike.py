from bike.models.base import db, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Bike(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String(20), nullable=False)