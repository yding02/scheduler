import argparse
import time
import os
from scheduler.io.save import *
from scheduler.io.load import *
import globals

def do_nothing():
  return

def get_category_names_to_id(categories):
  names = {}
  for category in categories:
    names[category['name']] = category['id']
  return names
  
def input_category(category_names):
  while True:
    category = input("Category: ").lower().strip()
    if category not in category_names:
      c = input("Category does not exist, continue [Y/n]?")
      if c.lower() == "n":
        continue
      else:
        description = input("Description: ")
        categories = load_categories()
        id = categories[-1]['id'] + 1
        write_category_entry(id, category, description)
        category_names[category] = id
        return category
    else:
      return category

def add_schedule_entry():
  categories = load_categories()
  name = input("Name: ")
  description = input("Description: ")
  print("existing categories:")
  category_names = get_category_names_to_id(categories)
  for name in category_names:
    print(name, end = ' ')
  print()
  category = input_category(category_names)
  write_schedule_entry(time.time(), category_names[category], name, description)
  return   
  
def init():
  c = input("WARNING: will overwrite old data [y/N]: ")
  if c.lower() != "y":
    return
  if not os.path.exists("data"):
    os.makedirs("data")
  write_schedule_entry(time.time(), 0, "HEAD", "HEAD sentinel", type = "w")
  write_category_entry(0, "sentinel", "category for sentinels", type = "w")
  return

def main():
  #initialize global variables
  globals.init()
  
  parser = argparse.ArgumentParser(description='Record your schedule.')
  parser.add_argument('--init', action='store_const', dest='accumulate', const=init, default = do_nothing, help="initiates the scheduler")
  parser.add_argument('-a', '--add-entry', action='store_const', dest='accumulate', const=add_schedule_entry, 
    default = do_nothing, help="adds an entry to the schedule")
  args = parser.parse_args()
  args.accumulate()

  
if __name__ == "__main__":
  main()


