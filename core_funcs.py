# Core functionality

# Import standard packages
import sqlite3
from datetime import datetime
import config
import support_funcs
import database_funcs
import status_checks

def added_datetime():
    """Gets the current datatime to be added to transactions and when a new tracker is created"""
    dt = datetime.now()
    return dt

def add_tracker_item():
    """ Creates a dictionary of values to pass to the sqlite function to update the master_tracker table """

    # Get the tracker name and then run a check against the master_tracker table to check for dupes
    tracker_name = input("Please enter a name for your tracker: ")
    if status_checks.check_for_tables() == True:
        pass   # The check_for_tables will return False if there are no values found in maser_trackers table
    else:
        dupe = True
        while dupe == True:
            dupe_response = support_funcs.string_dup_check(tracker_name, database_funcs.list_active_trackers())
            if dupe_response == True:
                print("Duplicate. Please enter a new tracker name: ")
                tracker_name = input("Please enter a name for your tracker: ")
            else:
                dupe = False

    # Grab a string description of the tracker, is allowed to be empty
    tracker_description = input("Enter a description: ")

    # Get the type of tracker and run a check to ensure it is a correct option
    print("Tracker Types: Num (n) | Bool (b) | String (s)")
    type = input("Select the type of this tracker: ")
    while type.lower() not in config.tracker_types:
        type = input("Select the type of this tracker: ")

    # Convert to standard three options
    if type == 'n':
        type = 'Num'
    elif type == 'b':
        type = 'Bool'
    else:
        type = 'String'

    dt = added_datetime()

    di = {"name":tracker_name,
          "desc":tracker_description,
          "type":type,
          "dt":dt}

    print("Success, tracker created")
    return di


def add_numerical_transaction():
    """Adds a transaction to the "tracker_transactions" database of numerical tracker type"""
    tracker_id = input("Select Tracker: ")

    # Get the user to input the value
    input_val = ""
    try:
        input_val = input("Value: ")
    except:
        print("Please input a number value.")
    tracker_num_val = float(input_val)

    # Add datetime to when the transaction was added
    dt = added_datetime()

    # Leave blank to ensure no errors
    tracker_bool_val = ""
    tracker_string_val = ""

    di = {"tracker_id":tracker_id,
            "dt": dt,
            "tracker_num_val":tracker_num_val,
            "tracker_bool_val": tracker_bool_val,
            "tracker_string_val": tracker_string_val
            }
    return di

def add_bool_transaction():
    """Adds a transaction to the "tracker_transactions" database of bool tracker type"""
    tracker_id = input("Select Tracker: ")

    # Get the user to input the value
    input_val = input("True / False: ")
    if input_val in config.bool_true_possible_values:
        input_val = 1
    elif input_val in config.bool_false_possible_values:
        input_val = 0
    else:
        print("Error")

    tracker_bool_val = input_val

    # Add datetime to when the transaction was added
    dt = added_datetime()

    # Leave blank to ensure no errors
    tracker_num_val = ""
    tracker_string_val = ""

    di = {"tracker_id":tracker_id,
            "dt": dt,
            "tracker_num_val":tracker_num_val,
            "tracker_bool_val": tracker_bool_val,
            "tracker_string_val": tracker_string_val
            }
    return di

def add_string_transaction():
    """Adds a transaction to the "tracker_transactions" database of string tracker type"""
    tracker_id = input("Select Tracker: ")

    # Get the user to input the value
    input_val = input("True / False: ")
    if input_val in config.bool_true_possible_values:
        input_val = 1
    elif input_val in config.bool_false_possible_values:
        input_val = 0
    else:
        print("Error")

    tracker_bool_val = input_val

    # Add datetime to when the transaction was added
    dt = added_datetime()

    # Leave blank to ensure no errors
    tracker_num_val = ""
    tracker_string_val = ""

    di = {"tracker_id":tracker_id,
            "dt": dt,
            "tracker_num_val":tracker_num_val,
            "tracker_bool_val": tracker_bool_val,
            "tracker_string_val": tracker_string_val
            }
    return di