import re


def validate_username(username):

    if len(username) < 3 or len(username) > 10:
        return False
    return True


def validate_password(password):
    list_error = []

    if len(password) < 4:
        list_error.append("The length of the password should be at least 4")
    if not re.search(r'[A-Z]', password):
        list_error.append("At least one capital letter")

    if not re.search(r'[a-z]', password):
        list_error.append("At least one lowercase letter")
    if not re.search(r'\d.*\d', password):
        list_error.append("At least two numbers")

    if list_error:
        for error in list_error:
            print(f'*{error}')
        return False
    else:
        return True


