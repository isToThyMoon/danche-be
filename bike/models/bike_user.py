from bike.models.base import db, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Bike_user(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(10), nullable=False)
    mobile = Column(String(12))