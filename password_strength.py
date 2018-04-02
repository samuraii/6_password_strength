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
    special_chars = re.findall(r'[^\w\s]', password)
    return len(special_chars) if len(special_chars) < 2 else 2


def get_unique_word_patterns(password):
    return set(re.findall(r'[a-zA-Z]+', password))


def get_all_blacklist_words():
    with open('blacklist.txt') as file_content:
        return file_content.read().split()


def list_items_to_lower_case(list):
    resulting_list = []
    for word in list:
        resulting_list.append(word.lower())
    return resulting_list


def check_blacklist_words(password):
    word_patterns = get_unique_word_patterns(password)
    word_patterns_lowered = list_items_to_lower_case(word_patterns)
    blacklist = get_all_blacklist_words()
    not_in_blacklist_words = set(word_patterns_lowered) - set(blacklist)
    unique_words_count = len(not_in_blacklist_words)
    return unique_words_count if unique_words_count < 3 else 4


def get_password_strength(password):
    password_checklist = [
        check_special_characters,
        check_case_sensitivity,
        check_blacklist_words,
        check_letters_and_digits
    ]
    score = 0
    for score_function in password_checklist:
        score += score_function(password)
    return 'Your password score is {}'.format(score)


if __name__ == '__main__':
    user_password = get_password_from_user()
    password_strength = get_password_strength(user_password)
    print(password_strength)
