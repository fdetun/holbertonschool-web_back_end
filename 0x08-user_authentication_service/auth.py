#!/usr/bin/env python3
"""DB module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode(
            encoding='utf-8',
            errors='strict'),
        bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registering og user method"""
        try:
            userquery = self._db.find_user_by(email=email)
            if userquery:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            if email and password:
                obj = self._db.add_user(email, _hash_password(password))
                return obj
