#MAPEO DE LA BBDD CON PYTHON

from sqlalchemy import Column, Integer, BigInteger, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Rol(Base):
    __tablename__ = "rol"
    __table_args__ = {'schema':'scrum'}

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20))

class Prioridad(Base):
    __tablename__ = "prioridad"
    __table_args__ = {'schema': 'scrum'}

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20))



