import random

def play_word_guessing_game():
    """
    Play the word guessing game.
    """
    # Dictionary containing words as keys and their hints as values
    words_with_hints = {
        "apple": "a fruit",
        "banana": "also a fruit",
        "orange": "a fruit",
        "tomato": "a fruit",
        "carrot": "a vegetable",
        "broccoli": "a vegetable",
        "grapes": "a fruit",
        "strawberry": "a fruit",
        "watermelon": "a fruit",
        "pineapple": "a fruit",
        "spinach": "a vegetable",
        "avocado": "a fruit",
        "potato": "a vegetable",
        "pepper": "a vegetable",
        "lemon": "a fruit",
        "cucumber": "a vegetable",
        "peach": "a fruit",
        "pear": "a fruit",
        "kiwi": "a fruit",
        "cauliflower": "a vegetable"
    }

    # Choose a random word and its corresponding hint from the dictionary
    random_word, hint = random.choice(list(words_with_hints.items()))
    letter_guesses = 0
    incorrect_word_guesses = 0
    score = 20  # Initialize the score

    print(f"Hint: {hint}")

    # Game loop
    while incorrect_word_guesses < 3:
        # Get user guess
        guess = input("Guess a letter or the word: The answer is a fruit or vegetable ").lower()

        # Process user guess
        if len(guess) == 1:  # Single letter guess
            letter_guesses += 1
            if guess in random_word:
                count = random_word.count(guess)
                print(f"The letter {guess} is in the word {count} time(s).")
            else:
                print(f"The letter '{guess}' is not in the word.")
            score -= 1  # Deduct 1 point for a letter guess
        elif len(guess) == len(random_word):  # Full word guess
            if guess == random_word:
                print("Congratulations! You guessed the word correctly!")
                break
            else:
                incorrect_word_guesses += 1
                print("Incorrect guess! Try again.")
                score -= 5  # Deduct 5 points for an incorrect word guess
        else:  # Invalid guess
            incorrect_word_guesses += 1
            print("Incorrect guess! Try again.")

    # Display game outcome
    if incorrect_word_guesses == 3:
        print(f"The correct word was: {random_word}")
        print("You lose!")
    else:
        print(f"Your total points are {score}")

play_word_guessing_game()
