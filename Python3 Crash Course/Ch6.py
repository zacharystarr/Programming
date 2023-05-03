alien_0 = {"color": "green", "points" : 5 }
print(alien_0["color"])
print(alien_0["points"])

## Python keys can be any immutable data type - using a list will raise a TypeError

alien_0['x_position'] = 0
print(alien_0)

alien_0["color"] = "yellow"
print(alien_0)

del alien_0["points"]
print(alien_0)

favorite_languages = {
    "jen" : "Python",
    "sarah" : "c",
    "edward" : "ruby"
}

print(favorite_languages)

for key, value in favorite_languages.items():
    print(key)
    print(value)

for name in favorite_languages.keys():
    print(name)

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title())

for language in favorite_languages.values():
    print(language.title())



alien_0 = {"color": "Green", "points": 5}
alien_1 = {"color": "Yellow", "points": 10}
alien_2 = {"color": "Red", "points": 15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "pepperoni"]
}
for topping in pizza["toppings"]:
    print(topping)


users = {
    'aeinstein': {
        "first": "albert",
        "last": "einstein"
    },

    'mcurie': {
        "gender": "female",
        "profession": "scientist"

    }
}

for user in users.items():
    print(user)