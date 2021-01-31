# Core functionality

# Import standard packages

# Import program packages
import config
import support_funcs
import database_funcs
import status_checks


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
    new_type = input("Select the type of this tracker: ")
    while new_type.lower() not in config.tracker_types:
        new_type = input("Select the type of this tracker: ")

    # Convert to standard three options
    if new_type == 'n':
        new_type = 'Num'
    elif new_type == 'b':
        new_type = 'Bool'
    else:
        new_type = 'String'

    dt = support_funcs.added_datetime()

    di = {"name": tracker_name,
          "desc": tracker_description,
          "type": new_type,
          "dt": dt}

    print("Success, tracker created")
    return di


def add_numerical_transaction(trackerid):
    """Adds a transaction to the "tracker_transactions" database of numerical tracker type"""
    # tracker_id = input("Select Tracker: ")

    # Get the user to input the value
    input_val = ""
    try:
        input_val = input("Value: ")
    except:
        print("Please input a number value.")
    tracker_num_val = float(input_val)

    # Add datetime to when the transaction was added
    dt = support_funcs.added_datetime()

    # Leave blank to ensure no errors
    tracker_bool_val = ""
    tracker_string_val = ""

    di = {"tracker_id":trackerid,
            "dt": dt,
            "tracker_num_val":tracker_num_val,
            "tracker_bool_val": tracker_bool_val,
            "tracker_string_val": tracker_string_val
            }
    return di


def add_bool_transaction(trackerid):
    """Adds a transaction to the "tracker_transactions" database of bool tracker type"""
    # tracker_id = input("Select Tracker: ")

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
    dt = support_funcs.added_datetime()

    # Leave blank to ensure no errors
    tracker_num_val = ""
    tracker_string_val = ""

    di = {"tracker_id": trackerid,
          "dt": dt,
          "tracker_num_val": tracker_num_val,
          "tracker_bool_val": tracker_bool_val,
          "tracker_string_val": tracker_string_val
          }
    return di


def add_string_transaction(trackerid):
    """Adds a transaction to the "tracker_transactions" database of string tracker type"""
    #tracker_id = input("Select Tracker: ")

    # Get the user to input the value
    input_val = input("Text: ")
    tracker_string_val = input_val

    # Add datetime to when the transaction was added
    dt = support_funcs.added_datetime()

    # Leave blank to ensure no errors
    tracker_num_val = ""
    tracker_bool_val = ""

    di = {"tracker_id":trackerid,
            "dt": dt,
            "tracker_num_val":tracker_num_val,
            "tracker_bool_val": tracker_bool_val,
            "tracker_string_val": tracker_string_val
            }
    return di

def add_transaction(trackerid):
    """Used to select the type of add_tracker_"type" to the transaction_tracker table."""
    # Get the type of the tracker
    add_type = database_funcs.get_tracker_type(trackerid)
    print(add_type)

    if add_type == "Num":
        return add_numerical_transaction(trackerid)
    elif add_type == "Bool":
        return add_bool_transaction(trackerid)
    else:
        return add_string_transaction(trackerid)
