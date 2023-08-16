#!/usr/bin/env python3
"""Class for basic authentication"""

import base64
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
                encoded_str = base64_authorization_header.encode('utf-8')
                base64str = base64.b64decode(encoded_str)
                return base64str.decode()
        except:
            return None
