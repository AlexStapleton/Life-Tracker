# Main python run

import database_funcs
import core_funcs
import status_checks
import pprint

# Startup checks
if status_checks.run_db_existence_check() == False:
    database_funcs.create_default_tables()
    print("Database created")
else:
    pass

item = core_funcs.add_tracker_item()

database_funcs.add_master_tracker_table(item)

pprint.pprint(database_funcs.list_active_trackers())

value = core_funcs.add_numerical_transaction()
#value = core_funcs.add_bool_transaction()
database_funcs.add_tracker_transactions_table(value)