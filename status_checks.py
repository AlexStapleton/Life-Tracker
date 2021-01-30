# Checks on the system during setup

import pathlib
import os
import config
import database_funcs

### DB Existence Status ###
# Grab the db name from config.py
db_name = config.db_name

# Get current working directory
cwd = pathlib.Path().absolute()

# Try to find a current 'tracker.db' file
def find_db(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def run_db_existence_check():
    db_location = find_db(db_name,cwd)

    if db_location == None:
        db_exists = False
    else:
        db_exists = True
    return db_exists

def check_for_tables():
    """Checks to see if the master tracker and transaction tables have been created"""
    con = database_funcs.db_connection()
    connection = con[0]
    cursor = con[1]

    master_tracker_status = False
    tracker_transactions_status = False

    # Attempt to query the tables
    try:
        cursor.execute("""SELECT id FROM master_tracker""")
        master_tracker_status = True
    except:
        master_tracker_status = False

    try:
        cursor.execute("""SELECT id FROM racker_transactions""")
        tracker_transactions_status = True
    except:
        tracker_transactions_status = False

    return master_tracker_status
    return tracker_transactions_status