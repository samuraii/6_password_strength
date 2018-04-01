import re
import getpass
import sys


def get_password_from_user():
    user_password = getpass.getpass('Enter password (minimum len: 8):')
    if len(user_password) < 8:
        sys.exit('Password is too short.')
        return get_password_from_user()
    else:
        return user_password


def check_letters_and_digits(password):
    numbers = re.findall(r'[0-9]+', password)
    return len(numbers) if len(numbers) < 2 else 2


def check_case_sensitivity(password):
    lower_password = password.lower()
    upper_password = password.upper()
    if password != lower_password and password != upper_password:
        return 2
    else:
        return 0


def check_special_characters(password):
    return 0


def check_blacklist(password):
    with open('blacklist.txt') as file_content:
        black_list = file_content.read().split()
    return 0


def check_for_common_templates(password):
    return 0


def get_password_strength(password):
    password_checklist = [
        check_special_characters,
        check_case_sensitivity,
        check_blacklist,
        check_letters_and_digits,
        check_for_common_templates
    ]
    score = 0
    for score_function in password_checklist:
        score += score_function(password)

    return score


if __name__ == '__main__':
    user_password = get_password_from_user()
    password_strength = get_password_strength(user_password)
    print(password_strength)
