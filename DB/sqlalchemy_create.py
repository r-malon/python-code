from sqlalchemy import *
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker

Base = declarative.declarative_base()
engine = create_engine('sqlite:///teste.db', echo=True)
DBsession = sessionmaker(bind=engine)

class Client(Base):
	__tablename__ = 'client'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(64), nullable=False)
	#cpf = Column(String(20))

Base.metadata.create_all(engine)