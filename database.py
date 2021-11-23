from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = 'root'
SENHA = 'password'
HOST = 'localhost'
PORT = '5432'
BANCO = 'crud_usuario'

CONN = f"postgresql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

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
