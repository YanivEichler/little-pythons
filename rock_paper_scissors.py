import random
import sys


class RPS:
    def __init__(self):
        print("WELCOME TO ROCK PAPER SCISSORS")
        print("Tip: You can type only the first letter to choose your item!\n"
              "At any time, type 'quit' to quit.\n")

        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input('Rock, paper, or scissors? ').lower()
        if user_move == 'quit':
            print("Thanks for playing RPS!")
            sys.exit()
        if user_move in ['r','p','s']:
            if user_move == 'r':
                user_move = 'rock'
            elif user_move == 'p':
                user_move = 'paper'
            else:
                user_move = 'scissors'
        if user_move not in self.valid_moves:
            print("Invalid move, try again.")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print(f"Your move: {self.moves[user_move]}")
        print(f"AI Move: {self.moves[ai_move]}\n")

    def check_moves(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It's a tie!\n")
        elif (user_move == 'rock' and ai_move == 'scissors') or \
                (user_move == 'paper' and ai_move == 'rock') or \
                (user_move == 'scissors' and ai_move == 'paper'):
            print("You win!\n")
        else:
            print("You lose!\n")


if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()
