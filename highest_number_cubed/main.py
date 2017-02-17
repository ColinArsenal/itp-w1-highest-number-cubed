"""This is the entry point of the program."""


def highest_number_cubed(limit):
    x = 1
    for i in range(limit):
        while (x**3) <= limit:
            x += 1
    return (x -1)
         