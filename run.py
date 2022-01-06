import pyfiglet


def start_game():
    """
    Opens the title screen, requests players name and asks if player
    would like to see view rules and story.
    """
    print("\U0001f4a9" * 26)
    result = pyfiglet.figlet_format("DONT STEP\nIN THE\nPOOP")
    print(result)
    print("\U0001f4a9" * 26)

    name = input("Please enter your name: ")
    rules_response = input("Hi " + name + ". Would you like to see "
                           "the game rules & backstory? Enter y/n \n").lower()

    while rules_response not in ('y', 'n'):
        print("You have made an incorrect selection. Please try again\n")
        rules_response = input("Hi " + name + ". Would you like to see "
                               "the game rules & backstory? "
                               "Enter y/n \n").lower()

    if rules_response == 'y':
        game_rules()
    elif rules_response == 'n':

        ready_to_play = input("Are you ready to play? y/n \n").lower()

        while ready_to_play not in ('y', 'n'):
            print("You have made an incorrect selection. Please try again\n")
            ready_to_play = input("Are you ready to play? y/n \n").lower()

        if ready_to_play == 'y':
            open_game_board()
        if ready_to_play == 'n':
            print("You said NO!  Goodbye for now.\n")
            print("\U0001f4a9" * 22)
            result = pyfiglet.figlet_format("GOODBYE")
            print(result)
            print("\U0001f4a9" * 22)


def game_rules():
    """
    Displays game rules to user.
    Accepts user input and calls game function if user is
    ready to play.
    """
    print("HERE ARE THE RULES")

    ready_to_play = input("Are you ready to play? y/n \n").lower()

    while ready_to_play not in ('y', 'n'):
        print("You have made an incorrect selection. Please try again\n")
        ready_to_play = input("Are you ready to play? y/n \n").lower()

    if ready_to_play == 'y':
        open_game_board()
    elif ready_to_play == 'n':
        print("You said NO!  Goodbye for now.\n")
        print("\U0001f4a9" * 22)
        result = pyfiglet.figlet_format("GOODBYE")
        print(result)
        print("\U0001f4a9" * 22)


def open_game_board():
    """
    Opens game board ready to play or something like that
    """
    print("\U0001f4a9" * 22)
    print("GAME BOARD\n"
          "Top left corner is row 0, col 0.\n"
          "Bottom right corner is row 7, col 7.\n"
          "Make a clear path horizontally or vertically\n"
          "across the garden without stepping in dog poop! \U0001f4a9\n"
          "Good luck!")
    print("\U0001f4a9" * 22 + " \n")

    rows = (8)
    cols = (8)
    board = [["\U0001f7e9" for i in range(cols)] for j in range(rows)]

    for _ in board:
        print("".join(_))


start_game()
