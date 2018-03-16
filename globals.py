def init():
  global SCHEDULE_PATH, CATEGORY_PATH
  global SCHEDULE_PATTERN, CATEGORY_PATTERN
  SCHEDULE_PATH = "data/schedule"
  CATEGORY_PATH = "data/category"
  
  SCHEDULE_PATTERN = {
    'time' : None,
    'category': None,
    'name' : None,
    'description' : None,
  }

  CATEGORY_PATTERN = {
    'id' : None,
    'name' : None,
    'description' : None,
    'hidden' : None,
  }
  