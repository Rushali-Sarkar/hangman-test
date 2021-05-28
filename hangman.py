import string
from words import choose_word
from images import IMAGES

def is_word_guessed(secret_word: str, letters_guessed: [str]) -> bool:
    are_all_letters_guessed = [True if letter in letters_guessed else False for letter in secret_word]
    return all(are_all_letters_guessed)

def get_guessed_word(secret_word: str, letters_guessed: [str]) -> str:
    final_guessed_letters = [" " + each + " " if each in letters_guessed else ' _ ' for each in secret_word]
    return "".join(final_guessed_letters)


def get_available_letters(letters_guessed: [str]) -> str:
    ALL_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    return "".join([each if each not in letters_guessed else "" for each in ALL_LETTERS])


def hangman(secret_word: str) -> bool:
    
    attempts = 0
    print("I am thinking of a word that is ", get_guessed_word(secret_word, []), " letters long")
    letters_guessed = []
    
    while attempts < len(IMAGES) - 1:
        
        print("Hangman: ")
        print(IMAGES[attempts])
        
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: ", available_letters)
        guess = input("Please guess a letter from the available letters: ")
        letter = guess.lower()
    
        if letter not in available_letters:
            print("Sorry guess from the available letter basket")
            print(available_letters)
            print("Letters Guessed Till Now: ")
            print(get_guessed_word(secret_word, letters_guessed))
            
        elif letter in secret_word:
            letters_guessed.append(letter)
            if is_word_guessed(secret_word, letters_guessed):
                print("Wow you have guessed the word")
                print("You have a mind reading talent")
                print("The Word is: ")
                print(get_guessed_word(secret_word, letters_guessed))
                print("You are the Winner for this round!")
                return True
            else:
                print("Good guess")
                print("The word becomes: ")
                print(get_guessed_word(secret_word, letters_guessed))

        else:
            print("Sorry, that letter doesnot exsist in the word I am thinking")
            attempts += 1
            print("Please guess the word fast before the Hangman is hanged!")
            print("You have ", len(IMAGES) - 1 - attempts, " wrong attempts left")
            print("The word to be guessed: ")
            print(get_guessed_word(secret_word, letters_guessed))

    print("Sorry You couldnot save the Hangman")
    print("The word I thought was", secret_word)
    print(IMAGES[attempts])
    return False


def playHangman() -> None:
    isplaying = True
    current_round = 1
    total_winnings = 0
    while isplaying:
    
        print("Welcome to Hangman ROUND", current_round)
        secret_word = choose_word()
        if hangman(secret_word):
            total_winnings += 1
        print("You have won", total_winnings, "out of", current_round, "rounds.")
        print("Do you wish to continue playing to the next round ? (yes/no)")
        descion = input()
        if 'y' in descion:
            current_round += 1
        else:
            isplaying = False
    return

playHangman()
