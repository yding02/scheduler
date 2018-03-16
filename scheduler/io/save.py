import globals

def write_category_entry(id, name, description, type = "a"):
  globals.CATEGORY_PATTERN['id'] = id
  globals.CATEGORY_PATTERN['name'] = name
  globals.CATEGORY_PATTERN['description'] = description
  f = open(globals.CATEGORY_PATH, type)
  f.write(repr(globals.CATEGORY_PATTERN) + '\n')
  f.close()
  return
  
def write_schedule_entry(t, category_id, name, description, type = "a"):
  globals.SCHEDULE_PATTERN['time'] = t
  globals.SCHEDULE_PATTERN['category'] = category_id
  globals.SCHEDULE_PATTERN['name'] = name
  globals.SCHEDULE_PATTERN['description'] = description
  f = open(globals.SCHEDULE_PATH, type)
  f.write(repr(globals.SCHEDULE_PATTERN) + '\n')
  f.close()
  return
  
  