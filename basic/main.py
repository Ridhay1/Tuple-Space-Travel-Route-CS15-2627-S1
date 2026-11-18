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

