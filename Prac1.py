def vaccum_cleaner(loc, status):
  if status == "Dirty":
    return "Suck"
  elif status == "Clean" and loc == 'A':
    return "Move right"
  else:
    return "Move left"

rooms = { 'A' : 'Dirty', 'B' : 'Dirty'}
loc = 'A'
n = len(rooms)
print("Starting : ", rooms)
print("Starting Location:", loc)
for i in range (n * 2):
  status = rooms[loc]
  action = vaccum_cleaner(loc, status)
  print("\nStep ",i+1," :")
  print("Location :",loc)
  print("Status:",status)
  print("Action :",action)
  if action == "Suck":
    rooms[loc] = "Clean"
  elif action == "Move right":
    loc = 'B'
  else:
    loc = 'A'

print("Location :",loc)
print("Rooms :",rooms)
