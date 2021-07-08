from models.models import User
from common.database import db_session


def get(user_id: int) -> User:
    return User.query.get(user_id)


def get_with_username(username: str):
    return User.query.filter_by(username=username).first()


def save(user: User):
    db_session.add(user)
    db_session.commit()

    return user