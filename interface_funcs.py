# Functions for selecting actions
# Standard packages


# Standard packages


# Program packages
import support_funcs
import config
import core_funcs
import database_funcs

def main_menu():
    """Main user menu that program will revert to each time an action is completed"""
    print("""________ Main Menu ________ \nPlease select one of the\nfollowing actions \n""")
          
    # Grabs the list of available main_menu options, and prints it
    menu_vals = support_funcs.id_print_dict(config.main_menu_actions)

    # Get the users input
    selection = ""

    while selection not in menu_vals:
        selection = input("Selection: ")
        if selection == "q" or "quit":
            exit()

    return selection
