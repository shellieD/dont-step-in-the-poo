from random import randrange


def set_up_game():
    """
    Selects a random row as a clear path through the board.
    Distributes a poo randomly to each other row.
    """

    clear_path = randrange(0, 8)
    print(clear_path)

    poos = []
    for i in range(8):
        if i != clear_path:
            poos.append((i, randrange(0, 8)))
    print(poos)

    while True:
        row = int(input("Choose a row \n"))
        validate_input(row)

        if validate_input(row):
            print("data is valid")
            break

    while True:
        column = int(input("Choose a column \n"))
        validate_input(column)

        if validate_input(column):
            print("data is valid")
            break

        coord = (row, column)
        player_guess = []

        if coord in poos:
            print("What a mess!!!")
        else:
            print("Phew, no poo there!!")
            player_guess.append(coord)
            print(player_guess)


def validate_input(value):
    """
    Checks that the value entered is within
    the range 0-7
    """
    try:
        if value not in range(0, 7):
            raise ValueError(
                f"Please choose a number between 0 and 7. You entered: {value}"
            )
    except ValueError as e:
        print(f"Invalid Data {e}. Please try again. ")
        return False

    return True


set_up_game()
