bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha','suzuki']
motorcycles[0] = "ducati"
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)

motorcycles.insert(1,'ducati')
del motorcycles[0]
print(motorcycles)

popped_motorcyle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)

motorcycles = ['honda', 'yamaha','suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = "suzuki"
motorcycles.remove(too_expensive)
print(motorcycles)

cars = ['bmw','audi','toyata','subarbu']


cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(cars)

cars = ['bmw','audi','toyata','subarbu']
cars.reverse()
print(cars)
print(len(cars))