import globals
from scheduler.io.save import *
from scheduler.io.load import *

globals.init()

def up():
  categories = load_categories()
  s = ""
  for category in categories:
    category['hidden'] = None
    s += repr(category) + "\n"
  f = open(globals.CATEGORY_PATH, 'w')
  f.write(s)
  f.close()
  return
  
def down():
  return
