#!/usr/bin/env python3
"""
BasicAuth class
"""
from api.v1.auth.auth import Auth


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
