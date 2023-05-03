magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone, that was a great magic show!")


for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

cubes = [value**3 for value in range(1,11)]
print(cubes)

players = ['charles', 'martina', 'michael', 'florence',"eli"]
print(players[0:3])
print(players[:4])
print(players[2:])


print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
print(my_foods)
print(friend_foods)

friend_foods = my_foods
my_foods.append("ice cream")
print(my_foods)
print(friend_foods)

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (400,100)
for dimension in dimensions:
    print(dimension)


## Style notes: careful on indentations (tabs vs. spaces), use max 79 characters per line, use blank lines for spacing