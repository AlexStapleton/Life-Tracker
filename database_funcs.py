# Updating the database

import sqlite3
import config
import support_funcs
import status_checks

# Get the db location from the config file
database_location = config.db_location
database_name = config.db_name

# Functions to create, manage, update the sqlite database


def db_connection():
    """Use to connect to the database and create a cursor"""
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    return [connection, cursor]


def create_default_tables():
    """ Creates the initial instance of the database and updates the
    config.py location of the database """

    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]

    # Create the master tracker database
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS master_tracker (
            id INTEGER PRIMARY KEY,
            trackertype TEXT NOT NULL,
            trackername TEXT NOT NULL,
            trackerdesc TEXT,
            dateadded DATETIME,
            state INTEGER NOT NULL
        )
    """)

    # Create the trackers transaction database
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracker_transactions (
            id INTEGER PRIMARY KEY,
            trackerid INTEGER NOT NULL,
            date DATETIME,
            num_val DOUBLE,
            bool_val INTEGER,
            string_val TEXT,
            FOREIGN KEY (trackerid) REFERENCES master_tracker (id)
        )
    """)

    connection.commit()


def unique_id_gen(table):
    """Grabs the largest id in the table (input into function)
    and adds 1 to get a unique id.
    If there is no value in the database, this function returns 1"""

    master_tracker_status = False

    new_id = 0
    if status_checks.check_for_tables() == False:
        new_id = 1
    else:
        # Initiate the connection
        con = db_connection()
        connection = con[0]
        cursor = con[1]

        # Create correctly formatted string for cursor to read
        query = "SELECT MAX(id) FROM %s" % (table,)

        cursor.execute(query)
        max_id = cursor.fetchall()
        try:
            new_id = str(int(max_id[0][0]) + 1)
        except TypeError:
            new_id = '1'

    return new_id


def add_master_tracker_table(update_dict):
    """Accepts a dictionary of values (add_tracker_item) for a single tracker
    to update the master_tracker list """
    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]

    # Parse dictionary values
    name = update_dict["name"]
    description = update_dict["desc"]
    date = update_dict["dt"]
    set_type = update_dict["type"]
    state = 1

    # Get a unique id
    new_id = unique_id_gen('master_tracker')

    cursor.execute("""
        INSERT INTO master_tracker
            (id, trackertype, trackername, trackerdesc, dateadded, state)
            VALUES (?, ?, ?, ?, ?, ?)""", (new_id, set_type, name, description, date, state))

    connection.commit()


def add_tracker_transactions_table(update_dict):
    """ Add a transaction to the tracker_transactions table """
    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]

    # Get a unique id
    new_id = unique_id_gen('tracker_transactions')

    # Parse dictionary values
    date = update_dict["dt"]
    trackerid = update_dict["tracker_id"]
    tracker_num_val = update_dict["tracker_num_val"]
    tracker_bool_val = update_dict["tracker_bool_val"]
    tracker_string_val = update_dict["tracker_string_val"]

    cursor.execute("""
        INSERT INTO tracker_transactions
            (id, trackerid, date, num_val, bool_val, string_val)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (new_id, trackerid, date, tracker_num_val, tracker_bool_val, tracker_string_val))

    connection.commit()


def list_active_trackers(tracker_type='all'):
    """Returns a list of the current trackers from the master_tracker table."""
    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]
    connection.row_factory = sqlite3.Row

    if tracker_type == 'all':
        cursor.execute("""
            SELECT id, trackername FROM master_tracker
        """)
    else:
        # Create correctly formatted string for cursor to read
        query = "SELECT id, trackername FROM master_tracker WHERE trackertype = %s" % (tracker_type,)
        cursor.execute(query)

    trackers_dict = support_funcs.convert_tup_to_dict(cursor.fetchall())

    current_trackernames = []
    for value in trackers_dict.values():
        current_trackernames.append(value)

    return current_trackernames


def get_tracker_type(trackerid):
    """Returns the tracker type of a specific tracker."""
    con = db_connection()
    connection = con[0]
    cursor = con[1]

    querey = "SELECT trackertype from master_tracker WHERE id = %s" % (trackerid,)
    cursor.execute(querey)
    rows = cursor.fetchall()
    trackertype = rows[0][0]
    return trackertype


def list_transactions_tracker(trackerid):
    """Gets all of the transactions for a tracker from the tracker_transactions table"""
    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]
    connection.row_factory = sqlite3.Row

    # Get the type of the tracker
    tracker_type = get_tracker_type(trackerid)

    column_to_grab = ""
    if tracker_type == "Num":
        column_to_grab == "num_val"
    elif tracker_type == "Bool":
        column_to_grab = "bool_val"
    else:
        column_to_grab = 'string_val'

    query = "SELECT id, date, %s FROM tracker_transactions WHERE trackerid = %s" % (column_to_grab, trackerid,)
    cursor.execute(query)
    transactions_dict = support_funcs.convert_tup_to_dict(cursor.fetchall())
    list_transactions = []
    for value in transactions_dict.values():
        list_transactions.append(value)

    return list_transactions


def remove_master_tracker(trackerid):
    """Removes a tracker from the master_tracker table"""
    # Initiate the connection
    con = db_connection()
    connection = con[0]
    cursor = con[1]

    # Create query string to delete
    query = "DELETE FROM master_tracker WHERE id = %s" % (trackerid,)

    cursor.execute(query)
    connection.commit()
    
    print("%s was deleted" % (trackerid))
