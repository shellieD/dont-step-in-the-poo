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
    
    name = input("Please enter your name: ")
    rules_response = input("Hi " + name + ". Would you like to see the game rules & backstory? Enter y/n \n").lower()

start_game()