# app/api/v1/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext # Password hash garne tool (Node ko Bcrypt jastai)

from app.database.session import SessionLocal, Base, engine
from app.models.user import User as UserModel
from app.schemas.user import UserCreatePlain, UserResponse,UserLoginSchema,TokenResponse

# token 
from app.core.security import create_access_token,create_refresh_token

# hashing things
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

# Initialize PasswordHash with the modern Argon2 algorithm
password_hash = PasswordHash((Argon2Hasher(),))

# 1. Database table sync layer (Express ko sequelize.sync() jastai)
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/auth", tags=["Authentication"])

# 2. Password Security Configuration Tool (Bcrypt automatic algorithm settings)
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hashing using pwdlib[argon2]

# 3. Paani ko Dhara setup injector function (Database connection session manager)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 4. THE REAL USER REGISTRATION ROUTE
@router.post("/register/plain", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_in: UserCreatePlain, db: Session = Depends(get_db)):
    print(user_in)
    
    # A. Check if user already exists (Duplicate Email logic mapping)
    existing_user = db.query(UserModel).filter(UserModel.email == user_in.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Yo email bata account agi nai banyacha sathi!"
        )
    
    # B. Plain password lai safely Hash (scramble) gareko (Express ko bcrypt.hash jastai)
    # hashed_pwd = pwd_context.hash(user_in.password)

    # hashed password by argon2
    hashed_password=password_hash.hash(user_in.password)
    
    # C. Create New User Model Object (Blueprint mapped metadata instance memory model mapping)
    new_user = UserModel(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password,
        auth_provider="local"
    )
    
    # D. Push data inside Neon Cloud Database!
    db.add(new_user)      # Step 1: Data pipeline state save sequence logic allocation queue
    db.commit()           # Step 2: Write logic locks permanently cloud memory parameters update
    db.refresh(new_user)  # Step 3: Cloud data engine auto assign random unique UUID string refresh lookup back
    
    return new_user       # UserResponse schema auto filtering: password field filtered automatically!




# login route and logic
# app/api/v1/endpoints/auth.py inside login_user endpoint

@router.post("/login", response_model=TokenResponse)
def login_user(user_in: UserLoginSchema, db: Session = Depends(get_db)):
    
    # 1. Identity credentials parsing verification logic checkpoint
    user = db.query(UserModel).filter(UserModel.email == user_in.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User"
        )
    
    # 2. Cryptographic matching validation checks
    is_password_correct = password_hash.verify(user_in.password, user.hashed_password)
    if not is_password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email athawa Password milena sathi!"
        )
        
    # 3. Secure Payload creation setup
    token_payload = {"sub": str(user.id), "email": user.email}
    
    jwt_access_token = create_access_token(data=token_payload)
    jwt_refresh_token = create_refresh_token(data=token_payload) # 👈 Refresh token built here!
    
    # 5. Delivery structured payload packaging return
    return {
        "access_token": jwt_access_token,
        "refresh_token": jwt_refresh_token,
        "token_type": "bearer",
        "user": user
    }