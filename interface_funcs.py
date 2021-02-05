# Functions for selecting actions
# Standard packages

<<<<<<< HEAD
=======
# Standard packages

>>>>>>> aa6a14c0247730eac0b004ec1969faed8c408ea1
# Program packages
import support_funcs
import config
import core_funcs
import database_funcs

def main_menu():
    """Main user menu that program will revert to each time an action is completed"""
    print("""________ Main Menu ________ \nPlease select one of the\nfollowing actions \n""")

<<<<<<< HEAD
    # Grabs the list of available main_menu options, and prints it
    menu_vals = support_funcs.id_print_dict(config.main_menu_actions)
=======
    # Update the main menu potential choices
    menu_vals = []

    for x in config.main_menu_actions:
        menu_vals.append(x)

    # Iterate through the main menu selection values and print

    for x in config.main_menu_actions:
        print(x ,"-", config.main_menu_actions[x])
>>>>>>> aa6a14c0247730eac0b004ec1969faed8c408ea1

    # Get the users input
    selection = ""

    while selection not in menu_vals:
        selection = input("Selection: ")
<<<<<<< HEAD
        if selection == "q" or "quit":
            exit()
=======
>>>>>>> aa6a14c0247730eac0b004ec1969faed8c408ea1

    return selection
