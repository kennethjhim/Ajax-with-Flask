# lines = open('application/us_passenger_trains.txt').readlines().strip()
print("kenneth".startswith('ken'))

with open('application/us_passenger_trains.txt', 'r') as f:
  choices = [l.strip() for l in f.readlines()]

suggestions = [s for s in choices if s.lower().startswith(q)]
suggestions.sort()
print(suggestions)