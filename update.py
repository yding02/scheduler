import schema_update.db_transition
import globals

globals.init()
s = input("Are you sure you want to update: [y/N] ")

if s.strip().lower() == 'y':
  schema_update.db_transition.up()
  globals.close_conn()