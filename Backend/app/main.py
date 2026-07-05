from fastapi import FastAPI
from app.api.v1.api import api_router

# app/main.py
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text # Database ma simple 'PING' query pathauna text use gareko
from app.database.session import SessionLocal, engine, Base

app=FastAPI(title='Ai-Powered Research Paper Recommendation System')
app.include_router(api_router,prefix='/api/v1')




# DB Connection Dhara setup helper
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🌐 LIVE CONNECTION TEST ENDPOINT
@app.get("/test-db-connection")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # PostgreSQL lai euta simple arithmetic operation call pathayeko 
        # Yesko matlab database live chha vane '1' return garcha instant query test ma
        result = db.execute(text("SELECT 1")).fetchone()
        
        if result:
            return {
                "status": "success",
                "database": "Neon PostgreSQL Cloud",
                "message": "Connection Super Successful! Cloud dynamic pipe stable chha."
            }
    except Exception as error:
        # If credentials, password or host url bigreko chha vane error details throw hunchha
        raise HTTPException(
            status_code=500,
            detail=f"Database connectivity failed! Real Error logs: {str(error)}"
        )

