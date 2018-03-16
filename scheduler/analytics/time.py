from ..io import load

def time_spent_by_category(start):
  times = {}
  events = load.load_events_after(start)
  events.insert(0, {'time' : start})
  for i in range(len(events) - 1):
    event = events[i]
    next_event = events[i + 1]
    category = next_event['category_id']
    times[category] = times.get(category, 0) + next_event['time'] - event['time']
  return times
  