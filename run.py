
""" Play a simple game of chance """
# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

import pyfiglet
import gameboard


def clear():
    """ Clears terminal

    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def start_game():
    """
    Displays title screen and asks for users name.
    Gives player option to view rules and story.
    Asks if player is ready to play.
    Calls relevant function once input is validated.
    """
    print("\U0001f4a9 " * 26)
    title = pyfiglet.figlet_format("DONT STEP\nIN THE\nPOOP")
    print(title)
    print("\U0001f4a9 " * 26)

    player_name = input("Please enter your name: ")

    rules_response = input(f"Hi {player_name}. "
                           "Would you like to see the game rules & backstory? "
                           "Enter y/n \n").lower()

    while rules_response not in ('y', 'n'):
        print("You have made an incorrect selection. Please try again\n")
        rules_response = input(f"Hi {player_name}. Would you like to see "
                               "the story & game rules? "
                               "Enter y/n \n").lower()

    if rules_response == 'y':
        game_rules()
    elif rules_response == 'n':

        ready_to_play = input("Are you ready to play? y/n \n").lower()

        while ready_to_play not in ('y', 'n'):
            print("You have made an incorrect selection. Please try again\n")
            ready_to_play = input("Are you ready to play? y/n \n").lower()

        if ready_to_play == 'y':
            set_up_game()
        if ready_to_play == 'n':
            goodbye()


def game_rules():
    """
    Displays game rules to user.
    Accepts user input and calls game function if user is
    ready to play.
    """
    clear()
    print("\U0001f4a9 " * 22)
    print(" \n")
    story = pyfiglet.figlet_format("STORY", font="bubble")
    print(story)
    print(
        " \n"
        "Hello Postie!  I see you have some very important \n"
        "letters to deliver! \U0001f4ec \n"
        " \n"
        "Unfortunately, some very naughty pooches \U0001f415  have also \n"
        "made a few deliveries at this house. \U0001f4a9 \n"
        " \n"
        "Can you make it across the garden without stepping \n"
        "in that stinky dog poop? \n"
        " \n"
        )
    print("\U0001f4a9 " * 22)
    print(" \n")
    input("Press enter to continue \n")

    clear()

    print("\U0001f4a9 " * 22)
    rules = pyfiglet.figlet_format("RULES", font="bubble")
    print(" \n")
    print(rules)
    print(
        " \n"
        "Make a horizontal path (L to R) across the garden using\n"
        "the numbers on your keypad to chose the row and column \n"
        "you would like to guess."
        " \n"
        "If the tile you pick does not contain poo, the tile will be\n"
        "replaced with a shoe. \U0001f97e \n"
        " \n"
        "If you step in poo it will be replaced with.... well you know... \n"
        "and you will need to try and make a new path! \n"
        " \n"
        "Step in 5 poos and it's game-over! \n"
        " \n"
        "NOTE:  There is only one wining row, so tread carefully! \n"
        " \n"
         )
    print("\U0001f4a9 " * 22)
    print(" \n")

    ready_to_play = input("Are you ready to play? y/n \n").lower()

    while ready_to_play not in ('y', 'n'):
        print("You have made an incorrect selection. Please try again\n")
        ready_to_play = input("Are you ready to play? y/n \n").lower()

    if ready_to_play == 'y':
        clear()
        set_up_game()
    elif ready_to_play == 'n':
        goodbye()


def validate_choice(user_choice):
    """
    Displays 'row' or 'column' string and gets user
    input for row or column chosen.
    Calls validate_input funtion to validate user
    input
    """
    while True:
        choice = input(f"Choose a {user_choice} ")

        if validate_input(choice):
            break
    return choice


def set_up_game():
    """ Instantiates the Board class

    * Accepts user input for row and column - must be number.
    * Validates input
    * Converts input into a tuple of 2 ints.
    * Appends tuple to player_guess in all events
    * Increments flat_poos if poo discovered
    * Appends tuple to correct_guess (if on clear path)
    * Calls end game functions if game won or lost.
    """
    clear()
    new_board = gameboard.Board()

    flat_poos = 0  # Stores amount of poos identified as int
    player_guess = []  # all player guesses (tuples of 2 ints)
    correct_guess = []  # correct guesses on clear path (tuples of 2 ints)

    while flat_poos < 5:

        clear()
        new_board.draw_board()

        coord = (validate_choice("row \n"), validate_choice("column \n"))
        coord_tuple = tuple(int(el) for el in coord)

        while coord_tuple in player_guess:
            print("Oh plop... you've already guessed that!! Try again")
            coord = (validate_choice("row \n"), validate_choice("column \n"))
            coord_tuple = tuple(int(el) for el in coord)

        player_guess.append(coord_tuple)

        if coord_tuple in new_board.poos:
            print("What a mess!!!")
            flat_poos = flat_poos + 1
            print(f"You stood in poo at coordinate: {coord_tuple}")
        elif coord_tuple in new_board.clear_path_coord:
            correct_guess.append(coord_tuple)
            print("Phew, no poo there!!")
            print(f"Clear path at coordinate: {coord_tuple}")
            if len(correct_guess) == 8:
                print("YOU WIN")
                you_win()
        else:
            print("Phew, no poo there!!")
            print(f"Clear path at coordinate: {coord_tuple}")

        print(f"You have stepped in {flat_poos} poos.")

        new_board.update_board(coord_tuple)

        sleep(3)
        clear()

    you_lose()


def you_lose():
    """
    Prints loose message to screen with ASCII art.
    Asks if player would like to play again
    """
    clear()
    print("\U0001f4a9 " * 22)
    print("\n")
    result = pyfiglet.figlet_format("* OH POOP * \n YOU LOOSE!")
    print(result)
    print("\U0001f4a9 " * 22)

    sleep(2)
    clear()

    print("\U0001f4a9 " * 22)
    print(" \n")
    print("                  #")
    print("                 {##} ")
    print("                {######} ")
    print("                {######}")
    print("              {###########} ")
    print("               {#########} ")
    print("            {#### ####### ##} ")
    print("             {##__######__#} ")
    print("          {###################} ")
    print("           {#####{______}#####} ")
    print("          {###################} ")
    print("         {######################}")
    print(" \n")
    print("\U0001f4a9 " * 22)
    print(" \n")

    play_again = input("Would you like to play again? y/n \n")
    while play_again not in ('y', 'n'):
        print("You have made an incorrect selection. Please try again\n")
        play_again = input("Would you like to play again? y/n \n").lower()

    if play_again == 'y':
        set_up_game()
    elif play_again == 'n':
        thanks()
        goodbye()


def you_win():
    """
    Prints win message to screen with ASCII art.
    Asks if player would like to play again.
    """
    clear()
    print("\U0001f4a9 " * 22)
    print("\n")
    result = pyfiglet.figlet_format("  * YAY * \n * YOU WIN!*")
    print(result)
    print("\U0001f4a9 " * 22)
    print(" \n")

    sleep(2)
    clear()

    print("\U0001f4a9 " * 22)
    print(" \n")
    print("             OOOOOOOOOOO")
    print("         OOOOOOOOOOOOOOOOOOO")
    print("      OOOOOO  OOOOOOOOO  OOOOOO")
    print("    OOOOOO      OOOOO      OOOOOO")
    print("  OOOOOOOO  #   OOOOO  #   OOOOOOOO")
    print(" OOOOOOOOOO    OOOOOOO    OOOOOOOOOO")
    print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    print("OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO")
    print(" OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO")
    print("  OOOO   OOOOOOOOOOOOOOOOOOO   OOOO")
    print("    OOOO   0OOOOOOOOOOOOOO   0OOO")
    print("     OOOOO    OOOOOOOOO    OOOOO")
    print("        OOOO             OOOO")
    print("           000000OOOOOOOOO")
    print(" \n")
    print("\U0001f4a9 " * 22)

    play_again = input("Would you like to play again? y/n \n")
    while play_again not in ('y', 'n'):
        print("You have made an incorrect selection. Please try again\n")
        play_again = input("Would you like to play again? y/n \n").lower()

    if play_again == 'y':
        set_up_game()
    elif play_again == 'n':
        thanks()
        goodbye()

def thanks():
    clear()
    print("\U0001f4a9 " * 22)
    thanks = pyfiglet.figlet_format("THANKS FOR \n PLAYING")
    print(thanks)
    print("\U0001f4a9 " * 22)
    sleep(2)

def goodbye():
    """
    Prints goodbye message and exits game.
    """
    # clear()
    # print("\U0001f4a9 " * 22)
    # thanks = pyfiglet.figlet_format("THANKS FOR \n PLAYING")
    # print(thanks)
    # print("\U0001f4a9 " * 22)
    # sleep(2)
    clear()
    print("\U0001f4a9 " * 22)
    good_bye = pyfiglet.figlet_format("GOODBYE")
    print(good_bye)
    print("\U0001f4a9 " * 22)
    exit()


def validate_input(value):
    """ Validates user input for row/column

    Within the first try statement, converts the row/column value entered
    into an integer.   Returns an error if value entered is not a number.

    Within the second try statement, returns an error if the number
    is not within the range 0-8
    """
    try:
        value = int(value)
    except ValueError:
        print(f"Invalid data: {value} is not a number")
        return False

    try:
        if value not in range(8):
            raise ValueError(f"Please choose a number between 0 and 7."
                             f"You entered: {value}")
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.")
        return False
    return True


start_game()
set_up_game()
