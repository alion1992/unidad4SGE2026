from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2:"
                       "//franciscoaliahernandez:@localhost"
                       ":5432/Tienda")

Session = sessionmaker(bind=engine)
session = Session()