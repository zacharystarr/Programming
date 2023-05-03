'''
message = input("Tell me something and I will repeat it back to you!: ")
print(message)

prompt = "Tell me more about yourself!"
prompt += "\nWhat is your first name? "

name=input(prompt)
print("\nHello " + name + "!")

age = input("How old are you?")
age = int(age)
print(age >= 18)

print(4 % 3) 
'''
current_number = 1
while current_number <=5:
    print(current_number)
    current_number+=1

'''
prompt = "\nSay something and I'll repeat it. Enter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else: 
        print(message)

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print("That's a cool city!")
'''
current_number=0
while current_number < 10:
    current_number+=1
    if current_number % 2 ==0:
        continue

    print(current_number)

# to modify a list you have to iterate through, use a while loop, not a for loop because there could be difficulty keeping track


unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("verifying " + current_user)
    confirmed_users.append(current_user)


pets = ["dog", "cat", "cat", "parrot"]
while 'cat' in pets:
    pets.remove('cat')

print(pets)


responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response


    repeat = input("Is there another vote? (Y/N)")
    if repeat == "N":
        polling_active = False
    
print("\nPoll Results")
print(responses)