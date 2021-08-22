

n = int(input())

ships = []

for i in range(n):
    ship = input()
    
    ships.append(ship)

carStr = [c for c in ships if "car" in c]
vel = [int(car) for car in carStr[0] if car.isdigit()]
print(vel)
print(carStr)
print(ships)