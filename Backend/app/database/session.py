
# app/db/session.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL=os.getenv('DATABASE_URL')

# create_engine(...): Yo bhaneko timro backend ra Neon cloud database biche ko "Thulo Paani ko Pipe" (Main Pipe) ho. Yesle real network connection line setup garchha.

# pool_pre_ping=True: Yo ekdam dactar (smart) feature ho. Yesle hare k choti database ma data halnu or hernu bhanda paila euta sano "Ping" (Hello) pathauchha: "Hello Neon cloud, timi active chhau ni? Line katya ta chaina?" If line katchha bhane yesle aafai naya connection line ready garchha, backend crash huna dindaina.
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Standard metadata dynamic tracker base object initialization instances
Base = declarative_base()