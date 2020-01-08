import sqlite3
import os

def processed_string(string):
  return str(string).strip().lower()

def init():
  global __DATA_PATH__, __DATA_DIR__
  global __EVENT_PATTERN__, __CATEGORY_PATTERN__
  global __EVENT_TYPES__, __CATEGORY_TYPES__
  global __conn__
  
  __DATA_DIR__ = "data"
  __DATA_PATH__ = __DATA_DIR__ + "/data.db"
  
  __EVENT_TYPES__ = {
    'id' : int, 
    'time' : int, 
    'category_id' : int, 
    'name' : processed_string, 
    'description' : str,
  }

  __CATEGORY_TYPES__ = {
    'id' : int, 
    'name' : processed_string, 
    'description' : str, 
    'hidden' : int,
  }
  
  __EVENT_PATTERN__ = ('id', 'time', 'category_id', 'name', 'description',)
  __CATEGORY_PATTERN__ = ('id', 'name', 'description', 'hidden',)
  
  start_conn()

def close_conn():
  global __conn__
  if not __conn__:
    return
  __conn__.close()
  
def start_conn():
  global __conn__
  if not os.path.exists(__DATA_DIR__):
    os.makedirs("data")
    print("Database does not exist yet! Please initiate with --init.")
  elif not os.path.exists(__DATA_PATH__):
    print("Database does not exist yet! Please initiate with --init.")
  __conn__ = sqlite3.connect(__DATA_PATH__)
  