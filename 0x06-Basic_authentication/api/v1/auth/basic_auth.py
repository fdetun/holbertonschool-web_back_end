#!/usr/bin/env python3
"""
BasicAuth class
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """Basic Auth that inhertis from Auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """base 64 parser"""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header.encode('utf-8')).decode('utf-8')
        except BaseException:
            pass

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """func extract_user_credentials"""
        None_Tuple = (None, None)
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None_Tuple
        if ':' not in decoded_base64_authorization_header:
            return None_Tuple
        cred = decoded_base64_authorization_header.split(':')
        return (cred[0], cred[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """get user from data function"""
        if user_email is None or user_pwd is None:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            obj = User()
            user = obj.search({'email': user_email})
            for i in user:
                if i.is_valid_password(user_pwd):
                    return i
            return None
        except BaseException:
            return None
