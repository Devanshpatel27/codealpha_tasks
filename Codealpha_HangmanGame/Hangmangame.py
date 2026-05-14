# Hangman Game - CodeAlpha Internship

import random 

def get_random_word():
    words = ["python", "hangman", "programming", "challenge", "developer",]
    return random.choice(words)

word = get_random_word()

word_length = len(word)
if word_length <= 5:
    hint_count = 2
elif word_length <= 8:
    hint_count = 3  
else:
    hint_count = 2


guessed_letters = random.sample(list(set(word)), hint_count)

wrong_guesses = 0
max_wrong = 6
print("Welcome to Hangman game!")

while wrong_guesses < max_wrong:

    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"\nWord: {display_word}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
    
        print("You already guessed that letter. Try again.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1
    
    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        break
else:    print(f"Game over! The word was: {word}")


