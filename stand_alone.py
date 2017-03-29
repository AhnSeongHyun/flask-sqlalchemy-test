# using SQLAlchemy without Flask-SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:xxxx@xxxxx/test', echo=True)
from sqlalchemy.orm import sessionmaker
from user import User
Session = sessionmaker(bind=engine)
session = Session()
print session.query(User).all()