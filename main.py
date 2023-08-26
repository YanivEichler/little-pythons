from random import choice


def main():
    secret_word: str = choice(["elephant", "computer", "mountain", "chocolate", "umbrella",
                               "pineapple", "giraffe", "hamburger", "notebook", "waterfall"])
    mistakes_left: int = 6

    player_name: str = input("Please enter your name: ")
    print(f"Welcome {player_name}! Let's play Hangman!")

    drawings = [
        """
          |----|
          |    
          |
        __|__
        """,
        """
          |----|
          |    O
          |
        __|__
        """,
        """
          |----|
          |    O
          |    |
        __|__
        """,
        """
          |----|
          |    O
          |   /|
        __|__
        """,
        """
          |----|
          |    O
          |   /|\\
        __|__
        """,
        """
          |----|
          |    O
          |   /|\\
        __|__ /
        """,
        """
          |----|
          |    O
          |   /|\\
        __|__ / \\
        """
    ]
    guessed_chars = []

    while True:
        print(drawings[6-mistakes_left])

        for c in secret_word:
            if c in guessed_chars:
                print(c, end='')
            else:
                print('_', end='')
        print("\n")  # blank line

        user_char: str = input("Make a guess: ").lower()
        if len(user_char) != 1:
            print("Invalid input, guess again!")
            continue
        if user_char not in secret_word:
            mistakes_left -= 1
            print(f"Nope! You have {mistakes_left} mistakes left.")
            if mistakes_left == 0:
                print(drawings[6])
                print(f"The secret word was: {secret_word}. Better luck next time!")
                break
        else:
            print("Nice!")
            guessed_chars.append(user_char)
            if len(set(secret_word)) == len(guessed_chars):
                print(f"You won! The word was: {secret_word}")
                break


if __name__ == '__main__':
    main()
