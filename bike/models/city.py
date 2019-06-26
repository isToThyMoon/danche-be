from bike.models.base import db, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(20), nullable=False)
    mode = Column(String(1))
    op_mode = Column(String(1))
    auth_status = Column(String(1))
    city_admin = Column(String(10))
    city_admin_id = Column(Integer)
    open_time = Column(String(50))
    update_time = Column(String(50), default=None)

    def to_json(self):
        return {
            'id': self.id,
            'city_name': self.city_name,
            'mode': self.mode,
            'op_mode': self.op_mode,
            'auth_status': self.auth_status,
            'city_admin': self.city_admin,
            'city_admin_id': self.city_admin_id,
            'open_time': self.open_time,
            'update_time': self.update_time
        }