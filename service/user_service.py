from models.models import User
from repository import user_repository
from exception.exceptions import InvalidCredentialsException, InvalidDataException
from os import environ
import bcrypt
import jwt
import time


def get(user_id: int) -> dict:
    user = user_repository.get(user_id)

    return user.get_dict() if user else user


def login(login_data: dict):
    user = user_repository.get_with_username(login_data['username'])
    if not user or len(login_data['password']) == 0:
        raise InvalidCredentialsException()

    if bcrypt.checkpw(login_data['password'].encode('utf-8'), user.password.encode('utf-8')):
        user_dict = user.get_dict()
        del user_dict['password']

        user_dict["iat"] = round(time.time() * 1000)
        user_dict["exp"] = round(time.time() * 1000) + 7200000 #2hours from now
        encoded_jwt = jwt.encode(user_dict, environ.get('JWT_SECRET'), algorithm=environ.get('JWT_ALGORITHM'))
        
        return { 'token': encoded_jwt }


def register(register_data: dict):
    if len(register_data['username']) == 0 or len(register_data['password']) == 0:
        raise InvalidDataException('Username or password is missing.')
    elif user_repository.get_with_username(register_data['username']):
        raise InvalidDataException('Administrator with this username already exists.')

    encrypted_password = bcrypt.hashpw(register_data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    admin = User(username=register_data['username'], password=encrypted_password)

    admin = user_repository.save(admin)

    return admin.get_dict()