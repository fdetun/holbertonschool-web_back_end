#!/usr/bin/env python3
"""DB module
"""
import bcrypt


def _hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode(
            encoding='utf-8',
            errors='strict'),
        bcrypt.gensalt())
