import random

def load_words():
    WORDLIST_FILE = './words.txt'
    words = open(WORDLIST_FILE)
    word_list = []
    for each in words:
        current_line_words = each.split()
        word_list += current_line_words
    return word_list

PROCESSED_WORD_LIST = load_words()

def choose_word():
    word_list = PROCESSED_WORD_LIST
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
