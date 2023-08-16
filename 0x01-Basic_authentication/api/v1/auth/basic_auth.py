#!/usr/bin/env python3
"""Class for basic authentication"""

import base64
import binascii
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic auth class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Method that extracts the base64 part of the authorization header"""
        if (
            authorization_header
            and isinstance(authorization_header, str)
            and authorization_header.startswith("Basic ")
        ):
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes the base64 authorization header string"""
        try:
            if base64_authorization_header and isinstance(
                base64_authorization_header, str
            ):
                encoded_str = base64_authorization_header.encode("utf-8")
                base64str = base64.b64decode(encoded_str)
                return base64str.decode()
        except binascii.Error:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts the user email and password from the
        decoded auth_header string
        """
        email = None
        password = None
        if (
            decoded_base64_authorization_header
            and isinstance(decoded_base64_authorization_header, str)
            and decoded_base64_authorization_header.find(":") != -1
        ):
            email, password = decoded_base64_authorization_header.split(":")

        return (email, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Gets the user object from the db"""
        if user_email and user_pwd:
            user = User()
            search_result = user.search({"email": user_email})
            if search_result:
                user = search_result[0]
                if user.is_valid_password(user_pwd):
                    return user
        return None
