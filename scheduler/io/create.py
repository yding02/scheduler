import globals
import sqlite3
import os
import time

def init_db():
  globals.close_conn()
  if not os.path.exists(globals.__DATA_DIR__):
    os.makedirs("data")
  if os.path.exists(globals.__DATA_PATH__):
    os.remove(globals.__DATA_PATH__)
  globals.start_conn()
  conn = globals.__conn__
  c = conn.cursor()
  c.execute('''CREATE TABLE categories(
                id INTEGER PRIMARY KEY ASC, 
                name TEXT, description TEXT, 
                hidden INTEGER);
            ''')
  c.execute('''CREATE TABLE events(
                id INTEGER PRIMARY KEY ASC,
                time DATETIME, 
                category_id INTEGER, 
                name TEXT, 
                description TEXT,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            );
            ''')
            
  globals.__CATEGORY_TYPES__
  
  c.execute('INSERT INTO categories(name, description, hidden) VALUES (?, ?, ?)', (
    globals.__CATEGORY_TYPES__["name"]("sentinel"), 
    globals.__CATEGORY_TYPES__["description"]("sentinel"), 
    globals.__CATEGORY_TYPES__["hidden"](1),
  ))
  c.execute('SELECT id FROM categories WHERE name = "sentinel"')
  id = c.fetchone()[0]
  c.execute('INSERT INTO events(time, category_id, name, description) VALUES (?, ?, ?, ?)', (
    globals.__SCHEDULE_TYPES__['time'](time.time()), 
    globals.__SCHEDULE_TYPES__['category_id'](id), 
    globals.__SCHEDULE_TYPES__['name']("HEAD"), 
    globals.__SCHEDULE_TYPES__['description']("HEAD"),
  ))
  conn.commit()
  return
  