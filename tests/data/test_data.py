"""Test data definitions."""


class UserData:
    """User test data."""
    VALID_USER = {
        'username': 'testuser@example.com',
        'password': 'TestPassword123!',
    }
    
    INVALID_USER = {
        'username': 'invalid@example.com',
        'password': 'WrongPassword',
    }
    
    ADMIN_USER = {
        'username': 'admin@example.com',
        'password': 'AdminPassword123!',
    }


class FormData:
    """Form test data."""
    REQUIRED_FIELDS = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone': '+1234567890',
    }
    
    INVALID_EMAIL = 'invalid-email'
    INVALID_PHONE = 'abc123'
