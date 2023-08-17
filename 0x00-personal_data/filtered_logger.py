#!/usr/bin/env python3
"""Function that formats log messages"""

import re
import logging
from typing import Tuple

PII_FIELDS = ("email", "ssn", "password", "phone", "ip")


def filter_datum(fields, redaction, message, separator):
    """
    Function that obsfucates key in field
    with redaction in message
    """
    input_string = message
    for key in fields:
        pattern = re.compile(rf"{key}=[^{separator}]+")
        input_string = re.sub(pattern, f"{key}={redaction}", input_string)

    return input_string


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
        return filter_datum(self.fields, self.REDACTION,
                            formatted, self.SEPARATOR).replace(';', '; ')


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
