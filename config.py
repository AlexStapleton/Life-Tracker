# Configuration options

# Local database location (use local path)
db_name = "tracker.db"
db_location = "/mnt/storage2/tracker-data"

# Boolean values during input
bool_true_possible_values = ['1', 'true', 'True', 't', 'T']
bool_false_possible_values = ['0', 'false', 'False', 'f', 'F']

# Types of trackers supported
tracker_types = ['num', 'n', 'bool', 'b', 'string', 's']

# Main Menu actions, used by interface_funcs.py
main_menu_actions = {"1":"Add new tracker",
                     "2":"Remove a tracker",
                     "3":"Log to a tracker",
                     "4": "View trackers",
                     "5":"View tracker values"}

# Calling the function based on main menu selection
main_menu_functions = {"1": "core_funcs.add_tracker_item()",
                       "2": "database_funcs.remove_master_tracker()",
                       "3": "core_funcs.add_transaction()",
                       "4": "database_funcs.list_active_trackers()",
                       "5": "database_funcs.list_transactions_tracker()"}
