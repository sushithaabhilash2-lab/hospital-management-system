from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import (
    verify_password,
    create_access_token,
)


def login_user(
    db: Session,
    email: str,
    password: str
):
    print("\n========== LOGIN DEBUG ==========")
    print("Email entered:", email)
    print("Password entered:", password)

    db_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    print("Database User:", db_user)

    if not db_user:
        print("❌ User not found")
        return None

    print("Stored Email:", db_user.email)
    print("Stored Password Hash:", db_user.password)

    password_ok = verify_password(password, db_user.password)

    print("Password Match:", password_ok)

    if not password_ok:
        print("❌ Password verification failed")
        return None

    print("✅ Password verified successfully")

    token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role.value,
        }
    )

    print("✅ JWT Token Created")

    return {
        "access_token": token,
        "token_type": "bearer",
    }