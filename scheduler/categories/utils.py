def get_category_names_to_id(categories):
  names = {}
  for category in categories:
    names[category['name']] = category['id']
  return names
  

