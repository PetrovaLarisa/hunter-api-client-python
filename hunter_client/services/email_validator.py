"""Service for email validation."""
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def validate_email(email: str) -> bool:
    """Validate an email address format."""
    return email and isinstance(email, str) and re.fullmatch(email_regex, email)
