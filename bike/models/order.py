from bike.models.base import db, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Order(Base):
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    bike_id = Column(Integer)
    user_id = Column(Integer)
    user_name = Column(String(10))
    mobile = Column(String(12))
    distance = Column(String(10))
    total_time = Column(String(10))
    state = Column(String(1))
    start_time = Column(String(24))
    end_time = Column(String(24))
    total_fee = Column(String(12))
    user_pay = Column(String(12))