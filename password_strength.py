import re
import getpass
import sys


def get_password_from_user():
    return getpass.getpass('Enter password (minimum len: 8):').strip()


def score_digits(user_password):
    max_score = 2
    numbers_in_password = re.findall(r'[0-9]+', user_password)
    return len(numbers_in_password) if len(numbers_in_password) < 2 else max_score


def score_case_sensitivity(user_password):
    max_score = 2
    lower_password = user_password.lower()
    upper_password = user_password.upper()
    if user_password != lower_password and user_password != upper_password:
        return max_score
    else:
        return 0


def score_special_characters(user_password):
    max_score = 2
    special_chars = re.findall(r'[^\w\s]', user_password)
    return len(special_chars) if len(special_chars) < 2 else max_score


def get_unique_word_patterns(user_password):
    return set(re.findall(r'[a-zA-Z]+', user_password))


def get_list_of_blacklist_words(path_to_blacklist):
    with open(path_to_blacklist) as file_content:
        return file_content.read().split("\n")


def transform_words_to_lower(list_of_words):
    return [word.lower() for word in list_of_words]


def score_unique_words(user_password, blacklist_words):
    max_score = 4
    word_patterns = get_unique_word_patterns(user_password)
    word_patterns_lowered = transform_words_to_lower(word_patterns)
    unique_words = set(word_patterns_lowered) - set(blacklist_words)
    unique_words_count = len(unique_words)
    return unique_words_count if unique_words_count < 3 else max_score


def get_password_strength(password, blacklist):
    password_checklist = [
        score_case_sensitivity,
        score_special_characters,
        score_unique_words,
        score_digits
    ]
    password_score = 0
    for score_function in password_checklist:
        if score_function is score_unique_words:
            password_score += score_function(password, blacklist)
        else:
            password_score = score_function(password)
    return password_score


if __name__ == '__main__':
    try:
        path_to_blacklist = sys.argv[1]
        blacklist_words = get_list_of_blacklist_words(path_to_blacklist) 
    except IndexError:
        sys.exit('Please, provide a blacklist file.')
    user_password = get_password_from_user()
    if len(user_password) < 8:
        sys.exit('Password is too short.')
    password_strength = get_password_strength(user_password, blacklist_words)
    print('Your password score is {}'.format(password_strength))
