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
