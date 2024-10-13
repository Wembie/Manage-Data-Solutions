from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Fruit(Base):
    __tablename__= "fruits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    sugar = Column(Float)