number_of_starters = {
    'Salad': 0,
    'Soup': 0,
    'Pasta': 0
}

number_of_main = {
    'Palak Paneer': 0,
    'Vegetable Biryani': 0,
    'Naan': 0
}

number_of_dessert = {
    'Ice Cream': 0,
    'Cake': 0,
    'Jalebi': 0
}

price = {
    'Salad': 40,
    'Soup': 60,
    'Pasta': 80,
    'Palak Paneer': 120,
    'Vegetable Biryani': 150,
    'Naan': 25,
    'Ice Cream': 70,
    'Cake': 150,
    'Jalebi': 80
}


def order_starter_menu():
    print('---------Starter Menu---------')
    print('1. Salad: 40')
    print('2. Soup: 60')
    print('3. Pasta: 80')
    print('4. Skip')
    starter = int(input('Enter starter: '))
    return starter


def order_main_menu():
    print('---------Main Menu---------')
    print('1. Palak Paneer: 120')
    print('2. Vegetable Biryani: 150')
    print('3. Naan: 25')
    print('4. Skip')
    main = int(input('Enter main: '))
    return main


def order_dessert_menu():
    print('---------Dessert Menu---------')
    print('1. Ice Cream: 70')
    print('2. Cake: 150')
    print('3. Jalebi: 80')
    print('4. Skip')
    dessert = int(input('Enter dessert: '))
    return dessert


ordering = True

while ordering:

    print('---------Order Menu (It is single serving or person)---------')

    starter = order_starter_menu()
    main = order_main_menu()
    dessert = order_dessert_menu()

    number_of_starters['Salad'] += 1 if starter == 1 else 0
    number_of_starters['Soup'] += 1 if starter == 2 else 0
    number_of_starters['Pasta'] += 1 if starter == 3 else 0

    number_of_main['Palak Paneer'] += 1 if main == 1 else 0
    number_of_main['Vegetable Biryani'] += 1 if main == 2 else 0
    number_of_main['Naan'] += 1 if main == 3 else 0

    number_of_dessert['Ice Cream'] += 1 if dessert == 1 else 0
    number_of_dessert['Cake'] += 1 if dessert == 2 else 0
    number_of_dessert['Jalebi'] += 1 if dessert == 3 else 0

    if (sum(number_of_starters.values()) == 0 and sum(number_of_main.values()) == 0 and sum(number_of_dessert.values()) == 0):
        print('Must order at least one item')
        continue

    order = input('Do you want to order more? (yes/no): ')
    ordering = True if order == 'yes' else 'Invalid' if order != 'no' else False
    if ordering == 'Invalid':
        print("Invalid Input!! Default: True")
        ordering = True

bill = 0

for starter in number_of_starters:
    bill += price[starter] * number_of_starters[starter]
    if number_of_starters[starter] == 0:
        continue
    print(starter, number_of_starters[starter], "=",
          price[starter] * number_of_starters[starter])

for main in number_of_main:
    bill += price[main] * number_of_main[main]
    if number_of_main[main] == 0:
        continue
    print(main, number_of_main[main], "=", price[main] * number_of_main[main])

for dessert in number_of_dessert:
    bill += price[dessert] * number_of_dessert[dessert]
    if number_of_dessert[dessert] == 0:
        continue
    print(dessert, number_of_dessert[dessert], "=",
          price[dessert] * number_of_dessert[dessert])

print('Your total bill is: ', bill)
