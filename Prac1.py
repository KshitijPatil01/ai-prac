
def vacuum_cleaner(loc, status):
    if status == "Dirty":
        return "Suck"
    elif loc == 'A':
        return "Move right"
    else:
        return "Move left"


rooms = {'A': 'Dirty', 'B': 'Dirty'}
loc = 'A'
step = 1

print("Starting:", rooms)
print("Starting Location:", loc)

while 'Dirty' in rooms.values():

    status = rooms[loc]
    action = vacuum_cleaner(loc, status)

    print("\nStep", step, ":")
    print("Location:", loc)
    print("Status:", status)
    print("Action:", action)

    if action == "Suck":
        rooms[loc] = "Clean"
    elif action == "Move right":
        loc = 'B'
    else:
        loc = 'A'

    step += 1

print("\nAll rooms are clean!")
print("Final Location:", loc)
print("Final Rooms:", rooms)
