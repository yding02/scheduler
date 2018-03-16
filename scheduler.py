import argparse
import time
import os

SCHEDULE_PATH = "data/schedule"
CATEGORY_PATH = "data/category"

SCHEDULE_PATTERN = {
  'time' : None,
  'category': None,
  'name' : None,
  'description' : None,
}

CATEGORY_PATTERN = {
  'id' : None,
  'name' : None,
  'description' : None,
}

def do_nothing():
  return

def load_categories():
  f = open("data/category", "r")
  categories = f.readlines()
  f.close()
  
  for i in range(len(categories)):
    if categories[i] == "":
      continue
    categories[i] = eval(categories[i])
  return categories

def add_category_entry(name, description):
  categories = load_categories()
  id = categories[-1]['id'] + 1
  CATEGORY_PATTERN['id'] = id
  CATEGORY_PATTERN['name'] = name
  CATEGORY_PATTERN['description'] = description
  f = open(CATEGORY_PATH, 'a')
  f.write(repr(CATEGORY_PATTERN) + '\n')
  f.close()
  return id

def input_category(category_names):
  while True:
    category = input("Category: ")
    if category not in category_names:
      c = input("Category does not exist, continue [Y/n]?")
      if c.lower() == "n":
        continue
      else:
        description = input("Description: ")
        id = add_category_entry(category, description)
        category_names[category] = id
        return category
    else:
      return category
  
def add_schedule_entry():
  categories = load_categories()
  name = input("Name: ")
  description = input("Description: ")
  print("existing categories:")
  category_names = {}
  for category in categories:
    print(category['name'], end = ' ')
    category_names[category['name']] = category['id']
  print()
  category = input_category(category_names)
  
  SCHEDULE_PATTERN['time'] = time.time()
  SCHEDULE_PATTERN['category'] = category_names[category]
  SCHEDULE_PATTERN['name'] = name
  SCHEDULE_PATTERN['description'] = description
  
  f = open(SCHEDULE_PATH, "a")
  f.write(repr(SCHEDULE_PATTERN) + '\n')
  f.close()
  return   
  
def init():
  c = input("WARNING: will overwrite old data [y/N]: ")
  if c.lower() != "y":
    return
  if not os.path.exists("data"):
    os.makedirs("data")
  SCHEDULE_PATTERN['time'] = time.time()
  SCHEDULE_PATTERN['category'] = 0
  SCHEDULE_PATTERN['name'] = "HEAD"
  SCHEDULE_PATTERN['description'] = "HEAD sentinel"
  ws = repr(SCHEDULE_PATTERN)
  f = open(SCHEDULE_PATH, "w")
  f.write(ws + '\n')
  f.close()
  
  CATEGORY_PATTERN['id'] = 0
  CATEGORY_PATTERN['name'] = "sentinel"
  CATEGORY_PATTERN['description'] = "category for sentinels"
  ws = repr(CATEGORY_PATTERN)
  f = open(CATEGORY_PATH, "w")
  f.write(ws + '\n')
  f.close()
  return

parser = argparse.ArgumentParser(description='Record your schedule.')
parser.add_argument('--init', action='store_const', dest='accumulate', const=init, default = do_nothing, help="initiates the scheduler")
parser.add_argument('-a', '--add-entry', action='store_const', dest='accumulate', const=add_schedule_entry, 
  default = do_nothing, help="adds an entry to the schedule")
args = parser.parse_args()
args.accumulate()
