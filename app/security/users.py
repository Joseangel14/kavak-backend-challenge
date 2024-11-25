from app.security.auth import get_password_hash, verify_password

fake_users_db = {
    "testuser": {
        "username": "testuser",
        "hashed_password": get_password_hash("password123"),
    }
}

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user
