# Functions that don't provide features or interactions with the database

from datetime import datetime
from pprint import pprint

# Converts a tuple to a dictionary
def convert_tup_to_dict(tup):
    dict1 = dict(tup)
    return dict1


def added_datetime():
    """Gets the current datatime to be added to transactions and when a new tracker is created"""
    now = datetime.now()
    dt = now
    return dt


# Checks for duplicates of a string
def string_dup_check(str_val, str_list, type='lower'):
    """Takes a string value and checks to see if it matches in all lowercase to a value in the provided list.
    If the value is in the string will return TRUE, if not then FALSE.
    Default to lowercase match, but can choose either exact or proper."""

    if type == 'lower':
        val = str_val.lower()
        end_list = []
        for x in str_list:
            end_list.append(x.lower())
    elif type == 'proper':
        val = str_val.proper()
        end_list = []
        for x in str_list:
            end_list.append(x.proper())
    else:
        val = str_val
        end_list = str_list

    if val in end_list:
        return True
    else:
        return False

# Nicer way to print dictionaries, used for showing active trackers

def id_print_dict(di):
    """Takes a dictionary and returns the dictionary as printed, and returns a list of the key values."""

    id_vals = []

    for x in di:
        id_vals.append(x)

    for y in di:
        print(y, "-", di[y])

    return id_vals


def main_menu_func_calls(name):
    """Takes a name of a main action from config.main_menu_actions and converts it to a callable function"""
    id_val = config.main_menu_actions.index(name)
    return config.main_menu_functions(id_val)
