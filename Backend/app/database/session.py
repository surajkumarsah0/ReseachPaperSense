
# app/db/session.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL=os.getenv('DATABASE_URL')

# 🚨 PRODUCTION ATTENTION: Yo address control mapping variables target string format framework chha
# Timro Neon Dashboard ko connection configuration selection parameters tab ma gayera 
# Connection String option parameters bata 'SQLAlchemy' type setup framework reference link string context yaha replace link lines lock gara.

# Engine configuration link active mechanism line setups
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Dhara Generator instance connection session makers rules setup mappings lock
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Standard metadata dynamic tracker base object initialization instances
Base = declarative_base()