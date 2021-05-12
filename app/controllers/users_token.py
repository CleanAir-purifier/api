from app.settings import db
from pydantic import BaseModel


class UserToken(BaseModel):
    purifier_id: int = 0
    user_token: str = ""


def save_user_token(user_token):
    purifier_data = db.users_token.insert_one(user_token.dict())
    if purifier_data:
        return "User token saved."
    return "Failed to save token."
