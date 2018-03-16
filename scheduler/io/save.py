import globals
import sqlite3
import os
  
def insert_category_entry(name, description, hidden, id = None):
  conn = globals.__conn__
  c = conn.cursor()
  if not id:
    c.execute('INSERT INTO categories(name, description, hidden) VALUES (?, ?, ?)', (
      globals.__CATEGORY_TYPES__["name"](name), 
      globals.__CATEGORY_TYPES__["description"](description), 
      globals.__CATEGORY_TYPES__["hidden"](hidden),
    ))
  else:
    c.execute('INSERT INTO categories(id, name, description, hidden) VALUES (?, ?, ?, ?)', (
      globals.__CATEGORY_TYPES__["id"](id), 
      globals.__CATEGORY_TYPES__["name"](name), 
      globals.__CATEGORY_TYPES__["description"](description), 
      globals.__CATEGORY_TYPES__["hidden"](hidden),
    ))    
  conn.commit()
  return
  
def insert_schedule_entry(t, category_id, name, description):
  conn = globals.__conn__
  c = conn.cursor()
  c.execute('INSERT INTO events(time, category_id, name, description) VALUES (?, ?, ?, ?)', (
    globals.__SCHEDULE_TYPES__['time'](t), 
    globals.__SCHEDULE_TYPES__['category_id'](category_id), 
    globals.__SCHEDULE_TYPES__['name'](name), 
    globals.__SCHEDULE_TYPES__['description'](description),
  ))
  conn.commit()
  return
  