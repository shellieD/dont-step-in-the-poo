import pyfiglet
import emoji

def start_game():
    """
    Opens the title screen, requests players name and asks if player
    would like to see view rules and story.
    """
    print("\U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9"
    "\U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9"
    "\U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9")
    result = pyfiglet.figlet_format("DONT STEP\nIN THE\nPOOP")
    print(result)
    print("\U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9"
    "\U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9"
    "\U0001f4a9 \U0001f4a9 \U0001f4a9 \U0001f4a9\n"
    )

    while True:
        name = input("Please enter your name: ")
        rules_response = input("Hi " + name + ". Would you like to see the game rules & backstory? Enter y/n \n").lower()

        validate_response(rules_response)

    return rules_response

def validate_response(rules_response):  
    if rules_response == 'y':
        print("GAME RULES")
    elif rules_response == 'n':
        ready_to_play = input("Are you ready to play? y/n \n").lower()
        if ready_to_play == 'y':
            print("SHOW GAME BOARD")
        if ready_to_play == 'n':
            print("You said NO!  Goodbye for now.")
    else:
        print("You have made an incorrect selection. Please try again\n")
        input("Press Enter to continue...")
    return True

start_game()