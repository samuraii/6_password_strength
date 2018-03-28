import re
import getpass


def get_password_from_user():
    user_password = getpass.getpass('Enter password (minimum len: 8):')
    if len(user_password) < 8:
        print('Password is too short.')
        return get_password_from_user()
    else:
        return user_password


def check_digits(password):
    pass


def check_case_sensitivity(password):
    pass


def check_special_characters(password):
    pass


def check_blacklist(password):
    pass


def check_for_common_templates(password):
    pass


def get_password_strength(password):
    password_checklist = [
        check_special_characters,
        check_case_sensitivity,
        check_blacklist,
        check_digits,
        check_for_common_templates
    ]
    pass


if __name__ == '__main__':
    get_password_from_user()
