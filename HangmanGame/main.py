import nltk
import random
from nltk.corpus import words

def choose_word():
    nltk.download('words')
    word_list = words.words()
    return random.choice([word.lower() for word in word_list if len(word) > 5])

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good job!")
        else:
            attempts -= 1
            print("Incorrect guess.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return
    
    print("\nGame over. The word was:", word)

if __name__ == "__main__":
    hangman()
