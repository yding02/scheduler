def get_category_names_to_id(categories):
  names = {}
  for category in categories:
    names[category['name']] = category['id']
  return names
  
def get_category_id_to_names(categories):
  names = {}
  for category in categories:
    names[category['id']] = category['name']
  return names
  