from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    'sqlite:///db.sqlite3',
    pool_pre_ping=True
)

session_local= sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()