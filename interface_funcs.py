# Functions for selecting actions

# Standard packages

# Program packages
import support_funcs
import config
import core_funcs
import database_funcs

def main_menu():
    """Main user menu that program will revert to each time an action is completed"""
    print("""________ Main Menu ________ \nPlease select one of the\nfollowing actions \n""")

    # Update the main menu potential choices
    menu_vals = []

    for x in config.main_menu_actions:
        menu_vals.append(x)

    # Iterate through the main menu selection values and print

    for x in config.main_menu_actions:
        print(x ,"-", config.main_menu_actions[x])

    # Get the users input
    selection = ""

    while selection not in menu_vals:
        selection = input("Selection: ")

    return selection
