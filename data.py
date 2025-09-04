import random

    
def get_user_data():
        email = f"testuser_{random.randint(1, 10000)}@example.com",
        password = "TestPass123"
        return email, password


def get_existing_user():
    email = "test_user1@mail.ru",
    password = "1234567"
    return email, password

    