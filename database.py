from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = 'root'
SENHA = 'password'
HOST = 'localhost'
PORT = '5432'
BANCO = 'crud_usuario'


CONN = "postgres://wunojgfktdysqc:7d307d0ba2bc2429203f8b7f0acbcf20b25cbd60204d8d55e586ea7f1977ed90@ec2-54-204-128-96.compute-1.amazonaws.com:5432/ddgc2scn5q8d15"

db_engine = create_engine(CONN)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()


def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
