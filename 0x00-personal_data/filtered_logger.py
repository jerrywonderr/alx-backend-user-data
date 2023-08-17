#!/usr/bin/env python3
"""Function that formats log messages"""

import re
import logging
from typing import Tuple, List

PII_FIELDS = ("email", "ssn", "password", "phone", "ip")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """obfuscate key in string"""
    for key in fields:
        message = re.sub(re.compile(rf"{key}=[^{separator}]+"),
                              f"{key}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        formatted = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, formatted, self.SEPARATOR
        ).replace(";", "; ")


def get_logger():
    """Returns a streamlined logger object"""
    # Create a logger named "user_data"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)

    # Prevent messages from being propagated to other loggers
    logger.propagate = False

    # Create a StreamHandler with RedactingFormatter
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
