import globals
import sqlite3

def load_sql(sql, pattern, args = tuple()):
  conn = globals.__conn__
  c = conn.cursor()
  items = []
  for row in c.execute(sql, args):
    item = {}
    for i in range(len(row)):
      item[pattern[i]] = row[i]
    items.append(item)
  return items

def load_categories_sql(sql, args = tuple()):
  return load_sql(sql, globals.__CATEGORY_PATTERN__, args)
  
def load_categories():
  return load_categories_sql('SELECT * FROM categories ORDER BY id;')
  
def get_category_id(name):
  conn = globals.__conn__
  c = conn.cursor()
  c.execute('SELECT id FROM categories WHERE name = ?', (name,))
  x = c.fetchone()
  if x:
    return x[0]
  else:
    return 1

def load_events_sql(sql, args = tuple()):
  return load_sql(sql, globals.__EVENT_PATTERN__, args)

def load_n_events(n):
  return load_events_sql('SELECT * FROM events ORDER BY time ASC LIMIT ?', (n,))
  
def load_events():
  return load_events_sql('SELECT * FROM events ORDER BY time DESC;')

def load_events_after(time):
  return load_events_sql('SELECT * FROM events WHERE time >= ? ORDER BY time ASC;', (
    globals.__EVENT_TYPES__['time'](time),
  ))
  