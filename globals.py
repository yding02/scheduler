import sqlite3

def init():
  global __DATA_PATH__, __DATA_DIR__
  global __SCHEDULE_PATTERN__, __CATEGORY_PATTERN__
  global __SCHEDULE_TYPES__, __CATEGORY_TYPES__
  global __conn__
  
  __DATA_DIR__ = "data"
  __DATA_PATH__ = __DATA_DIR__ + "/data.db"
  
  __SCHEDULE_TYPES__ = {
    'id' : int, 
    'time' : int, 
    'category_id' : int, 
    'name' : str, 
    'description' : str,
  }

  __CATEGORY_TYPES__ = {
    'id' : int, 
    'name' : str, 
    'description' : str, 
    'hidden' : int,
  }
  
  __SCHEDULE_PATTERN__ = ('id', 'time', 'category_id', 'name', 'description',)
  __CATEGORY_PATTERN__ = ('id', 'name', 'description', 'hidden',)
  
  start_conn()

def close_conn():
  global __conn__
  __conn__.close()
  
def start_conn():
  global __conn__
  __conn__ = sqlite3.connect(__DATA_PATH__)
  