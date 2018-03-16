import globals
import sqlite3

def load_categories():
  conn = globals.__conn__
  c = conn.cursor()
  categories = []
  for row in c.execute('''SELECT * FROM categories ORDER BY id'''):
    category = {}
    for i in range(len(row)):
      category[globals.__CATEGORY_PATTERN__[i]] = row[i]
    categories.append(category)
  return categories
  
def get_category_id(name):
  conn = globals.__conn__
  c = conn.cursor()
  c.execute('SELECT id FROM categories WHERE name = ?', (name,))
  x = c.fetchone()
  if x:
    return x[0]
  else:
    return 1
    