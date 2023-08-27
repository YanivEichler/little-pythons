import random


def roll_dice(num_of_dice: int) -> list[int]:
    if num_of_dice <= 0:
        raise ValueError
    rolls_output: list[int] = []
    for i in range(num_of_dice):
        random_roll: int = random.randint(1, 6)
        rolls_output.append(random_roll)
    return rolls_output


def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll? ")

            if user_input.lower() in ['exit', 'none', '0']:
                print("Thanks for using the dice simulator!")
                break

            print(*roll_dice(int(user_input)), sep=', ')

        except ValueError:
            print("Invalid input, please try again")


if __name__ == '__main__':
    main()
