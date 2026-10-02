from sqlalchemy import Column, Integer, String, Text
from database import Base

class UserFitness(Base):
    _tablename_ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    weight = Column(Integer)
    goal = Column(String)
    intensity = Column(String)
    plan = Column(Text)
