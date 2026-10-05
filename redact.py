import re

def redact(text: str) -> str:
    # Aadhaar: 12 digits, optionally spaced as 4-4-4
    text = re.sub(r"\b\d{4}\s?\d{4}\s?\d{4}\b", "XXXX XXXX XXXX", text)
    # PAN format
    text = re.sub(r"\b[A-Z]{5}\d{4}[A-Z]\b", "XXXXXXXXXX", text)
    return text