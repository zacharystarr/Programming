cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = "bmw"
print(car == "bmw")

car = "Audi"
print(car.lower() == "audi")
print(car)

requested_topping = "mushrooms"
if requested_topping != 'anchovies':
    print("No anchovies!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print((age_0>=21) or (age_1>=17))

requested_toppings = ["mushrooms", "onions", "pineapple", "green peppers"]
print("mushrooms" in requested_toppings)
print("anchovies" not in requested_topping)

age_1=17
if age_1 >= 18:
    print("You are old enough to vote!")
else: 
    print("You are too young to vote")

# python only executes one block in an if-elif-else change

age = 67
if age < 4:
    price = 0
elif age < 18:
    price = 5

elif age < 65:
    price = 15

else:
    price = 10

print(price)

for topping in requested_toppings:
    if topping == "green peppers":
        print("sorry, we are out")
    else:
        print("Adding" + topping)
requested_toppings = []
if requested_toppings: # this checks if list is empty - it will return False if so
    for topping in requested_toppings:
        print("Adding " + topping)
    print("Pizza finished!")
else:
    print("You want a plain pizza")


available_toppings = ['mushrooms',"olives", "green peppers", "pepperoni"]
requested_toppings = ["mushrooms", "fries", "pineapple"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping)
    else:
        print("Sorry, we don't have " +requested_topping)
print("Pizza done")