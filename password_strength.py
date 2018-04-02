import re
import getpass
import sys


def get_password_from_user():
    return getpass.getpass('Enter password (minimum len: 8):').strip()


def check_letters_and_digits(user_password):
    numbers_in_password = re.findall(r'[0-9]+', user_password)
    return len(numbers_in_password) if len(numbers_in_password) < 2 else 2


def check_case_sensitivity(user_password):
    lower_password = user_password.lower()
    upper_password = user_password.upper()
    if user_password != lower_password and user_password != upper_password:
        return 2
    else:
        return 0


def check_special_characters(user_password):
    special_chars = re.findall(r'[^\w\s]', user_password)
    return len(special_chars) if len(special_chars) < 2 else 2


def get_unique_word_patterns(user_password):
    return set(re.findall(r'[a-zA-Z]+', user_password))


def get_list_of_blacklist_words():
    with open('blacklist.txt') as file_content:
        return file_content.read().split()


def list_items_to_lower_case(list):
    resulting_list = []
    for word_in_list in list:
        resulting_list.append(word_in_list.lower())
    return resulting_list


def check_blacklist_words(user_password):
    word_patterns = get_unique_word_patterns(user_password)
    word_patterns_lowered = list_items_to_lower_case(word_patterns)
    blacklist_words = get_list_of_blacklist_words()
    not_in_blacklist_words = set(word_patterns_lowered) - set(blacklist_words)
    unique_words_count = len(not_in_blacklist_words)
    return unique_words_count if unique_words_count < 3 else 4


def get_password_strength(password):
    password_checklist = [
        check_special_characters,
        check_case_sensitivity,
        check_blacklist_words,
        check_letters_and_digits
    ]
    password_score = 0
    for score_function in password_checklist:
        password_score += score_function(password)
    return 'Your password score is {}'.format(password_score)


if __name__ == '__main__':
    user_password = get_password_from_user()
    if len(user_password) < 8:
        sys.exit('Password is too short.')
    password_strength = get_password_strength(user_password)
    print(password_strength)
