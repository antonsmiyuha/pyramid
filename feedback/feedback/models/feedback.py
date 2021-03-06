from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
)

from .meta import Base


class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    subject = Column(Text)
    message = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(Text)
    customer_ip = Column()
