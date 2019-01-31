# Challenge from SoloLearn

# minimum length 5
# maximum length 10
# at least one number
# at least one special character
# no spaces

import re

def pw_validator():
    pw = input("Please enter your password:")
    numbers = re.findall("[0-9]", pw)
    special = re.findall("[^A-Za-z0-9]", pw)
    if len(pw) < 5:
        print("Your password is too short. Please enter at least 5 characters.")
        return pw_validator()
    elif len(pw) > 10:
        print("Your password is too long. Please enter 10 characters at most.")
        return pw_validator()
    elif len(numbers) < 1:
        print("Your password must contain a number.")
        return pw_validator()
    elif len(special) < 1:
        print("Your password must contain a special character.")
        return pw_validator()
    else:
        print("Your password was entered correctly.")
        return

pw_validator()