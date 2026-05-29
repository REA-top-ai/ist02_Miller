from models import Image
from database import SessionLocal
from models import User
from auth import (
    hash_password,
    verify_password,
    create_token
)

def register_user(username, password):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == username
    ).first()

    if existing_user:
        db.close()
        return "USER EXISTS"

    new_user = User(
        username=username,
        password=hash_password(password)
    )

    db.add(new_user)
    db.commit()

    db.close()

    return "USER CREATED"

def login_user(username, password):
    db = SessionLocal()

    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        db.close()
        return None

    if not verify_password(password, user.password):
        db.close()
        return None

    token = create_token(username)

    db.close()

    return token

def save_image_info(username, prompt, image_path):

    db = SessionLocal()

    user = db.query(User).filter(
        User.username == username
    ).first()

    new_image = Image(
        prompt=prompt,
        image_path=image_path,
        user_id=user.id
    )

    db.add(new_image)

    db.commit()

    db.close()