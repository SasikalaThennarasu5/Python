class InvalidMarkError(Exception):
    """Raised when marks are out of valid range (0-100)."""
    pass

class EmptyMarksError(Exception):
    """Raised when no marks are provided."""
    pass
