import argparse
import time
import os
import scheduler.io.create
import scheduler.io.save
import scheduler.io.load
import scheduler.analytics.time
import scheduler.categories.utils
import globals

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  BRIGHT_RED = '\033[101m'
  UNDERLINE = '\033[4m'

def do_nothing():
  return
  
def input_category(category_names, create = True):
  while True:
    category = input("Category: ").lower().strip()
    if category not in category_names:
      if not create:
        print("Category does not exist, try again")
        continue
      c = input("Category does not exist, create [Y/n]?")
      if c.lower() == "n":
        continue
      else:
        description = input("Description: ")
        categories = scheduler.io.load.load_categories()
        scheduler.io.save.insert_category_entry(category, description, False)
        return category
    else:
      return category

def print_categories(categories, display_hidden = False):
  print("Existing categories: ")
  for category in categories:
    if category['hidden'] and not display_hidden:
      continue
    name = category['name']
    print(name)
      
def add_category_entry():
  categories = scheduler.io.load.load_categories()
  print_categories(categories, True)
  category_names = scheduler.categories.utils.get_category_names_to_id(categories)
  input_category(category_names)
  return
      
def add_schedule_entry():
  categories = scheduler.io.load.load_categories()
  name = input("Name: ")
  description = input("Description: ")
  print_categories(categories)
  category_names = scheduler.categories.utils.get_category_names_to_id(categories)
  category = input_category(category_names)
  scheduler.io.save.insert_event_entry(time.time(), 
    scheduler.io.load.get_category_id(category), 
    name, description)
  return 

def update_category_entry():
  categories = scheduler.io.load.load_categories()
  print_categories(categories, True)
  category_names = scheduler.categories.utils.get_category_names_to_id(categories)
  print("Category to update")
  category_name = input_category(category_names, False)
  id = category_names[category_name]
  c = None
  for category in categories:
    if category["id"] == id:
      c = category
      break
  s = input("Enter a new name (blank to keep): ")
  if s:
    category["name"] = s
  s = input("Enter a new description (blank to keep): ")
  if s:
    category["description"] = s
  s = input("Enter a new hidden attribute (blank to keep): ")
  if s:
    category["hidden"] = s
  scheduler.io.save.update_category_entry(
    category["id"], category["name"], category["description"], category["hidden"])
  return
  
def print_time_spent(events, category_ids):
  total_time = sum([events[key] for key in events])
  print(bcolors.WARNING, end = "")
  print('{0:<16} {1:<16} {2:<10}'.format('Category', 'Time (hrs)', 'Percentage'))
  print(bcolors.ENDC, end = "")
  keys = list(events.keys())
  keys.sort(key = lambda x : -events[x])
  for key in keys:
    print('{0:<16} {1:<16.2f} {2:<10.2f}'.format(category_ids[key], events[key] / 3600, events[key] / total_time * 100))
  return

def report_time_spent(start):
  events = scheduler.analytics.time.time_spent_by_category(start)
  categories = scheduler.io.load.load_categories()
  category_ids = scheduler.categories.utils.get_category_id_to_names(categories)
  print_time_spent(events, category_ids)  
  
def report_time_spent_input():
  current_time = time.time()
  offset = float(input("Start time (in hrs ago): "))
  start = current_time - offset * 60 * 60
  report_time_spent(start)
  return
  
def init():
  c = input("WARNING: will overwrite old data [y/N]: ")
  if c.lower() != "y":
    return
  scheduler.io.create.init_db()
  return

def backup():
  return  

def print_event(event, current_time, categories_to_id):
  print(bcolors.WARNING + 'Event date: {} | {:.2f} minutes ago'.format(time.ctime(event['time']), 
    (current_time - event['time']) / 60), bcolors.ENDC)
  print('Event name:', event['name'])
  print('Event category:', categories_to_id[event['category_id']])
  print('Event description:', event['description'])
  print()
  return
  
def log(n):
  categories = scheduler.io.load.load_categories()
  category_ids = scheduler.categories.utils.get_category_id_to_names(categories)
  events = scheduler.io.load.load_n_events(n)
  current_time = time.time()
  for event in events:
    print_event(event, current_time, category_ids)
  return
  
  
def main():
  #initialize global variables
  globals.init()
  
  parser = argparse.ArgumentParser(description='Record your schedule.')
  parser.add_argument('--init', action='store_const', dest='execute', 
    const=init, default = do_nothing, help="initiates the scheduler")
  parser.add_argument('-a', '--add-event', action='store_const', dest='execute', const=add_schedule_entry, 
    default = do_nothing, help="adds an entry to the schedule")
  parser.add_argument('--add-category', action='store_const', dest='execute', const=add_category_entry, 
    default = do_nothing, help="creates a new category")
  parser.add_argument('-r', '--report', nargs = "?", action='store', dest='report', type=float, const=-1,
    default = None, help="reports time spent in past [REPORT] hours or blank for prompt")
  parser.add_argument('--update-category', action='store_const', dest='execute', const=update_category_entry,
    default = do_nothing, help="creates a new category")
  parser.add_argument('--log', nargs = "?", action='store', dest='log', type=int, const=10,
    default = None, help="reports the past [LOG] events (10 by default)")
  args = parser.parse_args()
  args.execute()
  if args.report:
    if args.report == -1:
      report_time_spent_input()
    report_time_spent(time.time() - args.report * 3600)
  if args.log:
    log(args.log)
  globals.close_conn()
  
if __name__ == "__main__":
  main()
