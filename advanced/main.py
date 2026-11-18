mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print(mission_route[0])
print(mission_route[5])
print(len(mission_route))

for destination in mission_route:
    print(destination)

if "Europa" in mission_route:
    print("Europa is part of the mission route.")

destination = input("Enter a destination: ")

if destination in mission_route:
    print("Destination found!")
    position = mission_route.index(destination)
    print("Stops from the start:", position)

    stops_from_end = len(mission_route) - 1 - position
    print("Stops from end:", stops_from_end)

    if position < len(mission_route) - 1:
        print("Next stop:", mission_route[position + 1])
    else:
        print("This is the final stop of the journey.")

else:
    print("this destination is not part of the mission route.")