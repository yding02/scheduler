import argparse
import time
import os
from scheduler.io.create import *
from scheduler.io.save import *
from scheduler.io.load import *
import scheduler.analytics.time
from scheduler.categories.utils import *
import globals

def do_nothing():
  return
  
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
        insert_category_entry(category, description, False)
        return category
    else:
      return category

def print_categories(categories, display_hidden = False):
  print("Existing categories: ")
  for category in categories:
    if category['hidden'] and display_hidden:
      continue
    name = category['name']
    print(name, end = ' ')
  print()
      
def add_category_entry():
  categories = load_categories()
  print_categories(categories, True)
  category_names = get_category_names_to_id(categories)
  input_category(category_names)
  return
      
def add_schedule_entry():
  categories = load_categories()
  name = input("Name: ")
  description = input("Description: ")
  print_categories(categories)
  category_names = get_category_names_to_id(categories)
  category = input_category(category_names)
  insert_event_entry(time.time(), get_category_id(category), name, description)
  return 

def print_time_spent(events, category_ids):
  print('{0:<16} {1:<8}'.format('Category', 'Time (hrs)'))
  keys = list(events.keys())
  keys.sort(key = lambda x : -events[x])
  for key in keys:
    print('{0:<16} {1:<8.2f}'.format(category_ids[key], events[key] / 3600))
  return

def report_time_spent(start):
  events = scheduler.analytics.time.time_spent_by_category(start)
  categories = load_categories()
  category_ids = get_category_id_to_names(categories)
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
  init_db()
  return

def backup():
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
  args = parser.parse_args()
  if args.report:
    if args.report == -1:
      report_time_spent_input()
    report_time_spent(time.time() - args.report * 3600)
  args.execute()
  globals.close_conn()
  
if __name__ == "__main__":
  main()
