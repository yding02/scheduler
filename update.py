import schema_update.category.cat1
import globals

globals.init()
s = input("Are you sure you want to update: [y/N]")

if s.strip().lower() == 'y':
  schema_update.category.cat1.up()
