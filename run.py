import pyfiglet
import emoji

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
    rules_response = input("Hi " + name + ". Would you like to see the game rules & backstory? Enter y/n \n").lower()

    if rules_response == 'y':
        print("game_rules")
    elif rules_response == 'n':
        ready_to_play = input("Are you ready to play? y/n \n").lower()
        if ready_to_play == 'y':
                print("open_game_board")
        if ready_to_play == 'n':
            print("You said NO!  Goodbye for now.\n")
            print("\U0001f4a9" * 22)
            result = pyfiglet.figlet_format("GOODBYE")
            print(result)
            print("\U0001f4a9" * 22)
    else:
        print("You have made an incorrect selection. Please try again\n")

start_game()