import re

email_pattern = r'^[\w\.-]+@[\w\.-]+'


def validate_email(email):
    if re.match(email_pattern, email):
        return True
    return False


if __name__ == "__main__":
    email = input("Enter an email address: ")

    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
