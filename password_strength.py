import re
import getpass
import sys


def get_password_from_user():
    return getpass.getpass('Enter password (minimum len: 8):').strip()


def get_digits_score(user_password):
    max_score = 2
    numbers_in_password = re.findall(r'[0-9]+', user_password)
    if len(numbers_in_password) < max_score:
        return len(numbers_in_password)
    else:
        return len(numbers_in_password)


def get_case_sensitivity_score(user_password):
    max_score = 2
    lower_pass = user_password.lower()
    upper_pass = user_password.upper()
    sensetive = user_password != lower_pass and user_password != upper_pass
    return sensetive * max_score


def get_special_characters_score(user_password):
    max_score = 2
    special_chars = re.findall(r'[^\w\s]', user_password)
    return len(special_chars) if len(special_chars) < 2 else max_score


def get_unique_word_patterns(user_password):
    return set(re.findall(r'[a-zA-Z]+', user_password))


def get_list_of_blacklist_words(path_to_blacklist):
    with open(path_to_blacklist) as file_object:
        return file_object.read().split("\n")


def transform_words_to_lower(list_of_words):
    return [word.lower() for word in list_of_words]


def get_unique_words_score(user_password, blacklist_words):
    if not blacklist_words:
        return 0
    max_score = 4
    word_patterns = get_unique_word_patterns(user_password)
    word_patterns_lowered = transform_words_to_lower(word_patterns)
    unique_words = set(word_patterns_lowered) - set(blacklist_words)
    unique_words_count = len(unique_words)
    return unique_words_count if unique_words_count < 3 else max_score


def get_password_strength(password, blacklist):
    password_checklist = [
        get_case_sensitivity_score,
        get_special_characters_score,
        get_unique_words_score,
        get_digits_score
    ]
    password_score = 0
    for score_function in password_checklist:
        if score_function is get_unique_words_score:
            password_score += score_function(password, blacklist)
        else:
            password_score += score_function(password)
    return password_score


if __name__ == '__main__':
    try:
        path_to_blacklist = sys.argv[1]
        blacklist_words = get_list_of_blacklist_words(path_to_blacklist)
    except (IndexError, FileNotFoundError):
        print('Blacklist not passed or found, '
            'password won\'t be scored for unique words.')
        blacklist_words = None
    user_password = get_password_from_user()
    if len(user_password) < 8:
        sys.exit('Password is too short.')
    password_strength = get_password_strength(user_password, blacklist_words)
    print('Your password score is {}'.format(password_strength))
