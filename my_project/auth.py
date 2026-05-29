from passlib.context import CryptContext
from database import SessionLocal
from models import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def register_user(username: str, password: str):
    session = SessionLocal()

    existing_user = session.query(User).filter(User.username == username).first()

    if existing_user:
        session.close()
        print("User already exists")
        return None

    user = User(
        username=username,
        password=hash_password(password)
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()

    print("User created")
    return user


def login_user(username: str, password: str):
    session = SessionLocal()

    user = session.query(User).filter(User.username == username).first()

    if not user:
        session.close()
        print("User not found")
        return None

    if not verify_password(password, user.password):
        session.close()
        print("Wrong password")
        return None

    session.close()

    print("Login success")
    return user


def create_token():
    return None


def verify_token():
    return None