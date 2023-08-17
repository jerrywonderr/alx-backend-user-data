#!/usr/bin/env python3
"""Function that formats log messages"""

import re
import logging
from typing import List

PII_FIELDS = ("email", "ssn", "password", "phone", "ip")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """obfuscate key in string"""
    for key in fields:
        message = re.sub(
            re.compile(rf"{key}=[^{separator}]+"), f"{key}={redaction}", message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """ RedactingFormatter class. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Init """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Format """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


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
