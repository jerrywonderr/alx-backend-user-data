#!/usr/bin/env python3
"""Class for basic authentication"""

from api.v1.auth.auth import Auth


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
            return authorization_header[5:]
        return None
