from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Module_5.src.main.api.configs.config import Config


engine = create_engine(Config.fetch('databaseUrl'), echo=False)
SessionLocal = sessionmaker(bind=engine)