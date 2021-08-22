# Password Generator

from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(nr_letters=5, nr_numbers=2, nr_symbols=1):
    letters_sack = [choice(letters) for _ in range(nr_letters)]
    numbers_sack = [choice(numbers) for _ in range(nr_numbers)]
    symbols_stack = [choice(symbols) for _ in range(nr_symbols)]

    pass_list = letters_sack + numbers_sack + symbols_stack
    shuffle(pass_list)
    password = "".join(pass_list)

    return password
