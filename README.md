# Final
#Final


#fullcode

import os
import random

name = input("What's your name?\n")
print(f"Hello {name}! Let's play the word guessing game.")

file_path = "C:\\Users\\Nebiou\\Desktop\\WordGuessingGame\\words.txt"


if os.path.exists(file_path):
    with open(file_path, "r") as file:
        
        words = [word.strip() for word in file.readlines()]
        
    
    random_word = random.choice(words)


    
    letter_guesses = 0
    word_guesses = 0
    incorrect_word_guesses = 0
    guessed_word = ['_'] * len(random_word)

    
    while '_' in guessed_word and incorrect_word_guesses < 3:
        
      
        

        guess = input("Guess a letter or the word: The answer is a fruit or vegetable ").lower()
        
        
        if len(guess) == 1:
            letter_guesses += 1
            if guess in random_word:
                print(f"The letter {guess} is in the word {random_word.count(guess)} times.")
                
            else:
                print(f"The letter '{guess}' is not in the word.")
        
        
        elif len(guess) == len(random_word):
            word_guesses += 1
            if guess in random_word:
                print("Congratulations! You guessed the word correctly!")
                break
             
            else:
                incorrect_word_guesses += 1
                print("Incorrect guess! Try again.")
        else:
            incorrect_word_guesses += 1
            print("Incorrect guess! Try again.")
            

   
    if '_' not in guessed_word:
        score = letter_guesses
        print(f"Your score: {score} letter guesses.")

        
else:
    print(f"The file {file_path} does not exist.")


if incorrect_word_guesses == 3:
        print("You lose!")
        quit()

print(f"you guessed this letter {letter_guesses} times")
print(f"you guessed this word {incorrect_word_guesses} times")

total_points= 20
lose_letterguess=total_points-letter_guesses
points_for_inncorect=incorrect_word_guesses*5
tally=lose_letterguess-points_for_inncorect

if tally < 0:
    tally=0
    print("You lose!")


    
else:
    print(f"your total points is {tally}")




