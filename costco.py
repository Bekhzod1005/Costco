"""
choice = str(input("________ .Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an Item \n 4."))
while choice == "1" or choice == "2" or choice == "3":
    perm_options_1(choice)
    choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping "
                "list \n 3. Add an Item  \n 4. Go to the _____ section \n 5. Go to the _______section"))
if choice == "4":
    hunger[0] = hunger[0] + 1
    (hunger)
elif choice == "5":
    hunger[0] = hunger[0] + 1
    (hunger)
else:
    hunger[0] = hunger[0] + 1
    (hunger)
"""
from random import randint

sections = ["entrance", "electronics", "clothes", "household", "canned food", "pharmacy", "veggies & fruits", "meats", "frozen foods", "cash register", "dairy", "food court"]

clothes = ["Jacket", "Hat", "Nike pants", "T-shirt"]
electronics = ["Iphone 14", "TV", "Earbuds", "Alexa", "Tablet"]
household = ["Laundry powder", "Kettle", "Rug", "Utensils"]
veggies_fruits = ["Carrots", "Apples", "Tomatoes", "Grapes", "Potatoes"]
meats = ["Beef", "Chicken", "Salmon", "Pork"]
dairy = ["Yogurt", "Milk", "Cheese", "Butter"]
frozen_food = ["Frozen pizza", "Ice-cream", "Frozen berries", "Frozen fish fillets"]
canned_food = ["Canned peas", "Cannned corn", "Canned olives"]
pharmacy = ["Vitamin A", "Cod liver oil", "Ascorbic acid"]
food_court = ["Fries & Chicken", "Pizza", "Ice-cream", "Coke", "Poutine"]

shoppingList = []

all_products = [clothes, electronics, household, veggies_fruits, meats, dairy, frozen_food, canned_food, pharmacy]
for thingy in all_products:
    section = randint(0, 1)
    for i in range(section):
        product = randint(0, len(thingy)-1)
        shoppingList.append(thingy[product])

hunger = [0]
cart = []

#validation required 0-4
def entrance(hunger):
    choice = str(input("This is the starting point of your adventure, you are now located in the entrance area, "
                        "please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping "
                        "list \n 3. Go to the Clothes section \n 4. Go to the Electronics section \n "))
    while choice == "1" or choice == "2":
        perm_options_2(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping "
                        "list \n 3. Go to the Clothes section \n 4. Go to the Electronics section \n "))
    if choice == "3":
        hunger[0] = hunger[0] + 1
        clothes(hunger)
    else:
        hunger[0] = hunger[0] + 1
        electronics(hunger)

def electronics(hunger):
    choice = str(input(
        "hey you, looking for something fancy or casual? You are now in the electronics section, please indicate "
        "which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an Item \n 4.Go "
        "to the clothes section \n 5. go to the household Section \n"))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping "
                "list \n 3. Add an Item  \n 4. Go to the clothes section \n 5. Go to the household section"))
    if choice == "4":
        hunger[0] = hunger[0] + 1
        clothes(hunger)
    else:
        hunger[0] = hunger[0] + 1
        household(hunger)

def clothes(hunger):
    choice = str(input("Hello, you have now reached the clothes section of the costco store. Please indicate which "
                    "action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an Item "
                    "\n 4. Go to the Entrance \n 5. Go to the electronics section \n 6. Go to the canned food "
                    "section \n 7. Go to the pharmacy"))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping "
                "list \n 3. Add an Item  \n 4. Go to the Entrance \n 5. Go to the electronics section \n 6. Go to the canned food "
                "section \n 7. Go to the pharmacy"))
    if choice == "4":
        hunger[0] = hunger[0] + 1
        entrance(hunger)
    elif choice == "5":
        hunger[0] = hunger[0] + 1
        electronics(hunger)
    elif choice == "6":
        hunger[0] = hunger[0] + 1
        canned_food(hunger)
    else:
        hunger[0] = hunger[0]+1
        pharmacy(hunger)

def household(hunger):
    choice = str(input("You are in the household section, please indicate which action you want to perform: \n 1. "
                    "Show the map \n 2. Show the shopping list \n 3.Add an Item \n 4. Go to electronics section \n "
                    "5. Go to the fresh veggies/fruits section \n 6. Go to the meat section "))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the "
                        "shopping list \n 3. Add an Item  \n 4. Go to electronics section \n 5. Go to the fresh "
                        "veggies/fruits section \n 6. Go to the meat section"))
    if choice == "4":
        hunger[0] = hunger[0] + 1
        electronics(hunger)
    elif choice == "5":
        hunger[0] = hunger[0] + 1
        veggies_fruits(hunger)
    else:
        hunger[0] = hunger[0] + 1
        meats(hunger)

def canned_food(hunger):
    choice = str(input("Canned food everywhere! Please indicate which action you want to perform: \n 1. Show the map "
                    "\n 2. Show the shopping list \n 3. Add an Item \n 4. Go to the clothes section \n 5. Go to "
                    "the pharmacy\n 6. Go to the frozen foods section\n 7. Go to the cash register"))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map "
                    "\n 2. Show the shopping list \n 3. Add an Item \n 4. Go to the clothes section \n 5. Go to "
                    "the pharmacy\n 6. Go to the frozen foods section\n 7. Go to the cash register"))
    if choice == "4":
        hunger[0] = hunger[0] + 1
        clothes(hunger)
    elif choice == "5":
        hunger[0] = hunger[0] + 1
        pharmacy(hunger)
    elif choice == "6":
        hunger[0] = hunger[0] + 1
        frozen_food(hunger)
    else:
        hunger[0] = hunger[0] + 1
        cash_register(hunger)

def pharmacy(hunger):
    choice = str(input("Hi, you are now in the costco pharmacy, please indicate which action you want to perform: \n "
                    "1. Show the map \n 2. Show the shopping list \n 3.Add an Item \n 4. Go to the clothes section "
                    "\n 5. Go to the canned food section \n 6. Go to the cash register "))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the "
                        "shopping list \n 3. Add an Item  \n 4. Go to the clothes section \n 5. Go to the canned "
                        "food section \n 6. Go to the cash register "))
    if choice == "4":
        hunger[0] = hunger[0] + 1
        clothes(hunger)
    if choice == "5":
        hunger[0] = hunger[0] + 1
        canned_food(hunger)
    else:
        hunger[0] = hunger[0] + 1
        cash_register(hunger)

def veggies_fruits(hunger):
    choice = str(input("Veggies and fruits are right here! Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an Item \n 4. Go to the household section"))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item  \n 4. Go to the household section"))
    else:
        hunger[0] = hunger[0] + 1
        household(hunger)

def meats(hunger):
    choice = str(input("Looking for some meat? you are locate din the meat section of the store. Please indicate "
                    "which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an "
                    "Item \n 4. Go to the household section \n 5. Go to the frozen foods section \n 6. Go to the "
                    "dairy section"))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the "
                        "shopping list \n 3.Add an Item \n 4. Go to the household section \n 5. Go to the frozen "
                        "foods section \n 6. Go to the dairy section"))
    if choice == "4":
        hunger[0] = hunger[0] + 1
        household(hunger)
    elif choice == "5":
        hunger[0] = hunger[0] + 1
        frozen_food(hunger)
    else:
        hunger[0] = hunger[0] + 1
        dairy(hunger)

def frozen_food(hunger):
    choice = str(input("You are now in the frozen foods section, please indicate which action you want to perform: \n "
                    "1. Show the map \n 2. Show the shopping list \n 3.Add an Item \n 4. Go to the meat section \n "
                    "5. Go to the dairy section \n 6. Go to the canned food section"))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the "
                        "shopping list \n 3. Add an Item  \n 4. Go to the meat section \n 5. Go to the dairy "
                        "section \n 6. Go to the canned food section"))
    if choice == "4":
        hunger[0] = hunger[0] + 1
        meats(hunger)
    if choice == "5":
        hunger[0] = hunger[0] + 1
        dairy(hunger)
    else:
        hunger[0] = hunger[0] + 1
        canned_food(hunger)

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
def cash_register(hunger):
    pay = False
    choice = str(input("You are now at the cash register. Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Pay for the items \n 4. Go to the pharmacy \n 5. Go to the canned food section \n 6. Go to the food place"))
    while choice == "1" or choice  == "2":
        perm_options_2(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Pay for the items \n 4. Go to the pharmacy \n 5. Go to the canned food section \n 6. Go to the food place"))
    if choice == "3":
        pay = True
        choice == str(input("You have successfully paid for the items, please select what action you would like to do next \n"))
    elif choice == "4":
        hunger[0] = hunger[0] + 1
        pharmacy(hunger)
    elif choice == "5":
        hunger[0] = hunger[0] + 1
        canned_food(hunger)
    else:
        hunger[0] = hunger[0] + 1
        food_court(hunger)

def dairy(hunger):
    choice = str(input(
        "You are now in the fridge(Dairy section). Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an Item \n 4. Go to the meat section \n 5. Go to the frozen foods section"))
    while choice == "1" or choice == "2" or choice == "3":
        perm_options_1(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item  \n 4. Go to the meat section \n 5. Go to the frozen foods section"))
    if choice == "4":
        hunger[0] = hunger[0] + 1
        meats(hunger)
    else:
        hunger[0] = hunger[0] + 1
        frozen_food(hunger)

def food_court(hunger):
    choice = str(input(
        "FOOD! FOOD! FOOD! You are in the food court, please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. buy some food \n 4. GO to the cash register \n 5. go to the exit "))
    while choice == "1" or choice == "2" :
        perm_options_2(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. buy some food \n 4. Go to the cash register \n 5. go to the exit "))
    if choice == "3":
        hunger[0] = 0
    elif choice == "4":
        hunger[0] = hunger[0] + 1
        cash_register(hunger)
    else:
        hunger[0] = hunger[0] + 1
        exit(hunger)

def exit_area(hunger, pay):
    if pay:
        print("Congratulations! you have won the game and successfully survived in the Costco store. You can now go back home and do your homework now.")
        return 0
    else :
        choice = str(input("You can not leave the building until you purchase everything from the shopping list, please select an action you would like to perform \n 1. Check the map \n 2. Check the shopping list \n Go to the Food court \n"))

def display_map():
    pass

def shopping_list(shoppingList):
    x = 1
    print("Your shopping list:")
    for product in shoppingList:
        print(str(x) + "." + str(product))
        x += 1
    print("")

def add_item(cart):
    x = 1
    for thingy in all_products:
        for prod in range(len(thingy)):
            print(x + ". " + i[])
            x += 1
    object = str(input("Please select which object you would like to buy: "))
    print("You have added " + thingy[])

def perm_options_1(choice):
    if choice == "1":
        display_map()
    elif choice == "2":
        shopping_list(shoppingList)
    elif choice == "3":
        add_item()

def perm_options_2(choice):
    if choice == "1":
        display_map()
    elif choice == "2":
        shopping_list(shoppingList)

#actual code
print("Welcome to the Ultimate Costco Simulator. Here, you have to get out of Costco store by buying everything from "
    "the shopping list that your mom gave you. You also have a hunger bar and if it reaches 10 points - you lose. "
    "Moving from one section to another adds 1 hunger point to your hunger bar. Some product sections have free "
    "sample sections that subtract 3 hunger point from the hunger bar.")
entrance(hunger)
