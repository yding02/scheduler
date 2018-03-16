import globals
from scheduler.io.save import *
from scheduler.io.load import *

def load_categories_old():
  f = open(globals.CATEGORY_PATH, "r")
  categories = f.readlines()
  f.close()
  
  for i in range(len(categories)):
    if categories[i] == "":
      continue
    categories[i] = eval(categories[i])
  return categories
  
def load_schedules_old():
  f = open(globals.SCHEDULE_PATH, "r")
  schedules = f.readlines()
  f.close
  
  for i in range(len(schedules)):
    if schedules[i] == "":
      continue
    schedules[i] = eval(schedules[i])
  return schedules
  
  