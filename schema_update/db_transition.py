import globals
from scheduler.io.save import *
from scheduler.io.load import *
from scheduler.io.create import *

def load_categories_old():
  f = open("data/category", "r")
  categories = f.readlines()
  f.close()
  
  for i in range(len(categories)):
    if categories[i] == "":
      continue
    categories[i] = eval(categories[i])
  return categories
  
def load_schedules_old():
  f = open("data/schedule", "r")
  schedules = f.readlines()
  f.close
  
  for i in range(len(schedules)):
    if schedules[i] == "":
      continue
    schedules[i] = eval(schedules[i])
  return schedules

def up():
  init_db()
  categories = load_categories_old()
  for category in categories:
    if category['id'] == 0:
      continue
    insert_category_entry(category['name'], category['description'], category['hidden'] is not None, id = category['id'] + 1)
    
  schedules = load_schedules_old()
  for event in schedules:
    insert_schedule_entry(event['time'], event['category'] + 1, event['name'], event['description'])
  