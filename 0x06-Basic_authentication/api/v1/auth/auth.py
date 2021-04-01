from flask import Flask, jsonify, abort, request

class Auth:
    """ User Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth funct"""
        return False
    
    
    def authorization_header(self, request=None) -> str:
        """ auth header """
        return None

    
    def current_user(self, request=None) -> TypeVar('User'):
        """ current User"""
        return None
