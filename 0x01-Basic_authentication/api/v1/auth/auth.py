#!/usr/bin/python3
"""Base class for authentication"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a path requires auth
        args:
            - path (str) the path to be checked
            - excluded_paths (List) the paths that are originally excluded
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Checks the request object for an authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current auth user, else None"""
        return None
