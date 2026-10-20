import random

words = [
    "python",
    "computer",
    "programming",
    "developer",
    "website",
    "keyboard",
    "software",
    "database"
]

hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]


def play_hangman():
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n===== HANGMAN WORD GUESSING GAME =====")
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect guesses allowed.")

    while wrong_guesses < max_attempts:
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print(hangman_stages[wrong_guesses])
        print("Word:", display_word)
        print("Wrong guesses:", wrong_guesses, "/", max_attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            print("You win!")
            return

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print(hangman_stages[wrong_guesses])
    print("\nGame over! You ran out of attempts.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").lower().strip()

        if again not in ("yes", "y"):
            print("Thanks for playing Hangman!")
            break