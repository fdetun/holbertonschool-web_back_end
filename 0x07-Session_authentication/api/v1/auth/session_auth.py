#!/usr/bin/env python3
"""
BasicAuth class
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class SessionAuth(Auth):
    """Basic Auth that inhertis from Auth"""
    pass