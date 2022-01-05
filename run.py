import pyfiglet
import emoji

def start_game():
    """
    Opens the title screen and
    """
    print("\U0001f4a9" * 26)
    result = pyfiglet.figlet_format("DONT STEP\nIN THE\nPOOP")
    print(result)
    print("\U0001f4a9" * 26)
    
    name = input("Please enter your name: ")
    rules_response = input("Hi " + name + ". Would you like to see the game rules & backstory? Enter y/n \n").lower()

    