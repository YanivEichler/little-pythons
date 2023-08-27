import string
import secrets

def contains_upper(password: str) -> bool:
    for c in password:
        if c.isupper():
            return True
    return False


def contains_lower(password: str) -> bool:
    for c in password:
        if c.islower():
            return True
    return False


def contains_digit(password: str) -> bool:
    for c in password:
        if c.isdigit():
            return True
    return False

def contains_symbol(password: str) -> bool:
    for c in password:
        if c in string.punctuation:
            return True
    return False


def generate_password(pass_length: int, pass_upper: bool, pass_nums: bool, pass_syms: bool) -> str:
    available_chars: str = string.ascii_lowercase
    if pass_upper:
        available_chars += string.ascii_uppercase
    if pass_nums:
        available_chars += string.digits
    if pass_syms:
        available_chars += string.punctuation

    password: str = ''

    for x in range(pass_length):
        password += available_chars[secrets.randbelow(len(available_chars))]

    while True:
        if not contains_lower(password):
            password = generate_password(pass_length, pass_upper, pass_nums, pass_syms)
            continue
        elif pass_upper and not contains_upper(password):
            password = generate_password(pass_length, pass_upper, pass_nums, pass_syms)
            continue
        elif pass_nums and not contains_digit(password):
            password = generate_password(pass_length, pass_upper, pass_nums, pass_syms)
            continue
        elif pass_syms and not contains_symbol(password):
            password = generate_password(pass_length, pass_upper, pass_nums, pass_syms)
            continue
        else:
            break
    return password


if __name__ == '__main__':
    upper: bool = False
    nums: bool = False
    syms: bool = False
    length: int = 8
    amount_of_passwords: int = 1

    print("Hello user, this is a password generator.")
    while True:
        try:
            length: int = int(input("How many characters do you want in your password? "))
        except ValueError:
            print("Invalid input.")
            continue
        if length <= 0:
            print("Invalid length.")
            continue
        else:
            break

    while True:
        user_upper: str = input("Would you like the password to contain uppercase letters? [Y/N] ").lower()
        if user_upper not in ['y', 'n']:
            print("Invalid input.")
            continue
        elif user_upper == 'y':
            upper = True
            break
        else:
            break

    while True:
        user_nums: str = input("Would you like the password to contain digits? [Y/N] ").lower()
        if user_nums not in ['y', 'n']:
            print("Invalid input.")
            continue
        elif user_nums == 'y':
            nums = True
            break
        else:
            break

    while True:
        user_syms: str = input("Would you like the password to contain symbols? [Y/N] ").lower()
        if user_syms not in ['y', 'n']:
            print("Invalid input.")
            continue
        elif user_syms == 'y':
            syms = True
            break
        else:
            break

    while True:
        try:
            amount_of_passwords: int = int(input("How many passwords would you like to generate? "))
        except ValueError:
            print("Invalid input.")
            continue
        if amount_of_passwords <= 0:
            print("Invalid number.")
            continue
        else:
            break

    print("Your passwords:")
    for i in range(amount_of_passwords):
        print(generate_password(length, upper, nums, syms))

    print("\nThanks for using the password generator.")
