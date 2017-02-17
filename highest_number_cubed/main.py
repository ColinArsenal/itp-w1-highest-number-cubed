"""This is the entry point of the program."""


def highest_number_cubed(limit):
    cube = 1
    for num in range(limit):
        while (num ** 3) < limit:
            cube += 1
        return cube
         