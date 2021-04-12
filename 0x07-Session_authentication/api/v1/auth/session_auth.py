#!/usr/bin/env python3
"""
SessionAuth class
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class SessionAuth(Auth):
    """SessionAuth that inhertis from Auth"""
    pass
