"""
Bekhzod K
ICS3U
Costco simulation
Started: Jan 17, Finish: Jan 31
"""

from random import randint
import climage

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
cart_list = []

all_products = [clothes, electronics, household, veggies_fruits, meats, dairy, frozen_food, canned_food, pharmacy]

#Getting the randomized shopping list
for thingy in all_products:
    section = randint(0, 1)
    for i in range(section):
        product = randint(0, len(thingy)-1)
        shoppingList.append(thingy[product])



#validated
"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
def entrance():
    choice = str(input("This is the starting point of your adventure, you are now located in the entrance area, "
                        "please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping "
                        "list \n 3. Go to the Clothes section \n 4. Go to the Electronics section \n "))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
        choice = str(input("Incorrect input, must be between 1 and 4, please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Go to the Clothes section \n 4. Go to the Electronics section \n "))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Go to the Clothes section \n 4. Go to the Electronics section \n "))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            choice = str(input("Incorrect input, must be between 1 and 4, please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Go to the Clothes section \n 4. Go to the Electronics section \n "))
    if choice == "3":
        clothes()
    else:
        electronics()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def electronics(print_starting_message = True):
    if print_starting_message:
        print("hey you, looking for something fancy or casual? ")
    choice = str(input("You are now in the electronics section, please indicate "
        "which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. leave a product \n 6. Go "
        "to the clothes section \n 7. go to the household Section \n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7":
        choice = str(input("Incorrect input, the value should be between 1 and 7, please indicate "
                        "which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. leave a product \n 6. Go "
                        "to the clothes section \n 7. go to the household Section \n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. leave a product \n 6. Go "
                        "to the clothes section \n 7. go to the household Section \n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7":
            choice = str(input("Incorrect input, the value should be between 1 and 7, please indicate "
                        "which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. leave a product \n 6. Go "
                        "to the clothes section \n 7. go to the household Section \n"))
    if choice == "3":
        add_item(all_products[1])
        electronics(False)
    elif choice == "4":
        cart(cart_list)
        electronics(False)
    elif choice == "5":
        leave_item(cart_list)
        electronics(False)
    elif choice == "6":
        clothes()
    else:
        household()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def clothes(print_starting_message = True):
    if print_starting_message:
        print("Hello, you have now reached the clothes section of the costco store. ")
    choice = str(input("Please indicate which "
                    "action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item"
                    "\n 4. Show the cart \n 5. leave an Item \n 6. Go to the Entrance \n 7. Go to the electronics section \n 8. Go to the canned food "
                    "section \n 9. Go to the pharmacy\n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" and choice != "9":
        choice = str(input("Incorrect input, the value has to be between 1 and 9, please indicate which "
                        "action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item"
                    "\n 4. Show the cart \n 5. leave an Item \n 6. Go to the Entrance \n 7. Go to the electronics section \n 8. Go to the canned food "
                    "section \n 9. Go to the pharmacy\n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item"
                    "\n 4. Show the cart \n 5. leave an Item \n 6. Go to the Entrance \n 7. Go to the electronics section \n 8. Go to the canned food "
                    "section \n 9. Go to the pharmacy\n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" and choice != "9":
            choice = str(input("Incorrect input, the value has to be between 1 and 9, please indicate which "
                            "action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item"
                            "\n 4. Show the cart \n 5. leave an Item \n 6. Go to the Entrance \n 7. Go to the electronics section \n 8. Go to the canned food "
                            "section \n 9. Go to the pharmacy\n"))
    if choice == "3":
        add_item(all_products[0])
        clothes(False)
    elif choice == "4":
        cart(cart_list)
        clothes(False)
    elif choice == "5":
        leave_item(cart_list)
        clothes(False)
    elif choice == "6":
        entrance()
    elif choice == "7":
        electronics()
    elif choice == "8":
        canned_food()
    else:
        pharmacy()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def household(print_starting_message = True):
    if print_starting_message:
        print("You are in the household section, ")
    choice = str(input("Please indicate which action you want to perform: \n 1. "
                    "Show the map \n 2. Show the shopping list \n 3. Add an Item\n 4. Show the Cart \n 5. Leave an Item \n 6. Go to electronics section \n "
                    "7. Go to the fresh veggies/fruits section \n 8. Go to the meat section \n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" :
        choice = str(input("Invalid input, the value must be between 1 and 8, please indicate which action you want to perform: \n 1. "
                        "Show the map \n 2. Show the shopping list \n 3. Add an Item\n 4. Show the Cart \n 5. Leave an Item \n 6. Go to electronics section \n "
                        "7. Go to the fresh veggies/fruits section \n 8. Go to the meat section \n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the "
                        "shopping list \n 3. Add an Item  \n 4. Go to electronics section \n 5. Go to the fresh "
                        "veggies/fruits section \n 6. Go to the meat section\n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" :
            choice = str(input(
                "Invalid input, the value must be between 1 and 8, please indicate which action you want to perform: \n 1. "
                "Show the map \n 2. Show the shopping list \n 3. Add an Item\n 4. Show the Cart \n 5. Leave an Item \n 6. Go to electronics section \n "
                "7. Go to the fresh veggies/fruits section \n 8. Go to the meat section \n"))
    if choice == "3":
        add_item(all_products[2])
        household(False)
    elif choice == "4":
        cart(cart_list)
        household(False)
    elif choice == "5":
        leave_item(cart_list)
        household(False)
    elif choice == "6":
        electronics()
    elif choice == "7":
        veggies_fruits()
    else:
        meats()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def canned_food(print_starting_message = True):
    if print_starting_message:
        print("Canned food everywhere! ")
    choice = str(input("Please indicate which action you want to perform: \n 1. Show the map "
                    "\n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an item \n 6. Go to the clothes section \n 7. Go to "
                    "the pharmacy\n 8. Go to the frozen foods section\n 9. Go to the cash register\n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" and choice != "9":
        choice = str(input("Invalid input, the value should be between 1 and 7, please indicate which action you want to perform: \n 1. Show the map "
                    "\n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an item \n 6. Go to the clothes section \n 7. Go to "
                    "the pharmacy\n 8. Go to the frozen foods section\n 9. Go to the cash register\n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map "
                    "\n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an item \n 6. Go to the clothes section \n 7. Go to "
                    "the pharmacy\n 8. Go to the frozen foods section\n 9. Go to the cash register\n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" and choice != "9":
            choice = str(input(
                "Invalid input, the value should be between 1 and 7, please indicate which action you want to perform: \n 1. Show the map "
                    "\n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an item \n 6. Go to the clothes section \n 7. Go to "
                    "the pharmacy\n 8. Go to the frozen foods section\n 9. Go to the cash register\n"))
    if choice == "3":
        add_item(all_products[7])
        canned_food(False)
    elif choice == "4":
        cart(cart_list)
        canned_food(False)
    elif choice == "5":
        leave_item(cart_list)
        canned_food(False)
    elif choice == "6":
        clothes()
    elif choice == "7":
        pharmacy()
    elif choice == "8":
        frozen_food()
    else:
        cash_register()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def pharmacy(print_starting_message = True):
    if print_starting_message:
        print("Hi, you are now in the costco pharmacy. ")
    choice = str(input("Please indicate which action you want to perform: \n "
                    "1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the care \n 5. leave and Item \n 6. Go to the clothes section "
                    "\n 7. Go to the canned food section \n 8. Go to the cash register \n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" :
        choice = str(input("Incorrect input, the value should be between 1 and 8, please indicate which action you want to perform: \n "
                        "1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the care \n 5. leave and Item \n 6. Go to the clothes section "
                        "\n 7. Go to the canned food section \n 8. Go to the cash register \n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the "
                        "shopping list \n 3. Add an Item  \n 4. Go to the clothes section \n 5. Go to the canned "
                        "food section \n 6. Go to the cash register \n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" :
            choice = str(input(
                "Incorrect input, the value should be between 1 and 8, please indicate which action you want to perform: \n "
                "1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the care \n 5. leave and Item \n 6. Go to the clothes section "
                "\n 7. Go to the canned food section \n 8. Go to the cash register \n"))
    if choice == "3":
        add_item(all_products[8])
        pharmacy(False)
    elif choice == "4":
        cart(cart_list)
        pharmacy(False)
    elif choice == "5":
        leave_item(cart_list)
        pharmacy(False)
    elif choice == "6":
        clothes()
    elif choice == "7":
        canned_food()
    else:
        cash_register()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def veggies_fruits(print_starting_message = True):
    if print_starting_message:
        print("Veggies and fruits are right here! ")
    choice = str(input("Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the household section\n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        choice = str(input("Incorrect inout, the value must be between 1 and 6, Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the household section\n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the household section\n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
            choice = str(input(
                "Incorrect inout, the value must be between 1 and 6, Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the household section\n"))
    if choice == "3":
        add_item(all_products[3])
        veggies_fruits(False)
    elif choice == "4":
        cart(cart_list)
        veggies_fruits(False)
    elif choice == "5":
        leave_item(cart_list)
        veggies_fruits(False)
    else:
        household()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
# validated
def meats(print_starting_message = True):
    if print_starting_message:
        print("Looking for some meat? You are located in the meat section of the store. ")
    choice = str(input("Please indicate "
                    "which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an "
                    "Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the household section \n 7. Go to the frozen foods section \n 8. Go to the "
                    "dairy section\n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" :
        choice = str(input("invalid input, the value should be between 1 and 8, please indicate "
                        "which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an "
                        "Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the household section \n 7. Go to the frozen foods section \n 8. Go to the "
                        "dairy section\n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the "
                        "shopping list \n 3. Add an Item \n 4. Go to the household section \n 5. Go to the frozen "
                        "foods section \n 6. Go to the dairy section\n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" :
            choice = str(input("invalid input, the value should be between 1 and 8, please indicate "
                            "which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3.Add an "
                            "Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the household section \n 7. Go to the frozen foods section \n 8. Go to the "
                            "dairy section\n"))
    if choice == "3":
        add_item(all_products[4])
        meats(False)
    elif choice == "4":
        cart(cart_list)
        meats(False)
    elif choice == "5":
        leave_item(cart_list)
        meats(False)
    elif choice == "6":
        household()
    elif choice == "7":
        frozen_food()
    else:
        dairy()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def frozen_food(print_starting_message = True):
    if print_starting_message:
        print("You are now in the frozen foods section. ")
    choice = str(input("Please indicate which action you want to perform: \n "
                    "1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Add an Item \n 6. Go to the meat section \n "
                    "7. Go to the dairy section \n 8. Go to the canned food section\n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" :
        choice = str(input("Invalid input, must be between 1 and 8, Please indicate which action you want to perform: \n "
                    "1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Add an Item \n 6. Go to the meat section \n "
                    "7. Go to the dairy section \n 8. Go to the canned food section\n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Add an Item \n 6. Go to the meat section \n "
                    "7. Go to the dairy section \n 8. Go to the canned food section\n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"and choice != "6" and choice != "7" and choice != "8" :
            choice = str(
                input("Invalid input, must be between 1 and 8, Please indicate which action you want to perform: \n "
                    "1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Add an Item \n 6. Go to the meat section \n "
                    "7. Go to the dairy section \n 8. Go to the canned food section\n"))
    if choice == "3":
        add_item(all_products[6])
        frozen_food(False)
    elif choice == "4":
        cart(cart_list)
        frozen_food(False)
    elif choice == "5":
        leave_item(cart_list)
        frozen_food(False)
    elif choice == "6":
        meats()
    elif choice == "7":
        dairy()
    else:
        canned_food()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def cash_register():
    pay = False
    choice = str(input("You are now at the cash register. Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Pay for the items \n 4. Check the cart \n 5. Leave an Item \n 6. Go to the pharmacy \n 7. Go to the canned food section \n 8. Go to the food place\n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" :
        choice = str(input("Wrong input, the number must be between 1 and 8, Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Pay for the items \n 4. Check the cart \n 5. Leave an Item \n 6. Go to the pharmacy \n 7. Go to the canned food section \n 8. Go to the food place\n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Pay for the items \n 4. Go to the pharmacy \n 5. Go to the canned food section \n 6. Go to the food place\n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8":
            choice = str(input(
                "Wrong input, the number must be between 1 and 8, Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Pay for the items \n 4. Check the cart \n 5. Leave an Item \n 6. Go to the pharmacy \n 7. Go to the canned food section \n 8. Go to the food place\n"))
    if choice == "3":
        pay = True
        print("You have successfully paid for the product and you have been forced out of the cash register so...")
        food_court(pay)
    elif choice == "4":
        cart(cart_list)
        cash_register()
    elif choice == "5":
        leave_item(cart_list)
        cash_register()
    elif choice == "6":
        pharmacy()
    elif choice == "7":
        canned_food()
    else:
        food_court(pay)

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def dairy(print_starting_message = True):
    if print_starting_message:
        print("You are now in the fridge(Dairy section). ")
    choice = str(input("Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the meat section \n 7. Go to the frozen foods section\n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
        choice = str(input("Invalid inpit, the value has to be between 1 and 5, Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the meat section \n 7. Go to the frozen foods section\n"))
    while choice == "1" or choice == "2":
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the meat section \n 7. Go to the frozen foods section\n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
            choice = str(input(
                "Invalid inpit, the value has to be between 1 and 5, Please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Add an Item \n 4. Show the cart \n 5. Leave an Item \n 6. Go to the meat section \n 7. Go to the frozen foods section\n"))
    if choice == "3":
        add_item(all_products[5])
        dairy(False)
    elif choice == "4":
        cart(cart_list)
        dairy(False)
    elif choice == "5":
        leave_item(cart_list)
        dairy(False)
    elif choice == "6":
        meats()
    else:
        frozen_food()

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def food_court(pay):
    choice = str(input("FOOD! FOOD! FOOD! You are in the food court, please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Show the cart \n 4. Leave an Item \n 5. Go to the cash register \n 6. go to the exit \n"))
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        choice = str(input("Error, the input must be between 1 and 4, please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Show the cart \n 4. Leave an Item \n 5. Go to the cash register \n 6. go to the exit \n"))
    while choice == "1" or choice == "2" :
        perm_options(choice)
        choice = str(input("please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Show the cart \n 4. Leave an Item \n 5. Go to the cash register \n 6. go to the exit \n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
            choice = str(input("Error, the input must be between 1 and 4, please indicate which action you want to perform: \n 1. Show the map \n 2. Show the shopping list \n 3. Show the cart \n 4. Leave an Item \n 5. Go to the cash register \n 6. go to the exit \n"))
    if choice == "3":
        cart(cart_list)
        food_court()
    if choice == "4":
        leave_item(cart_list)
        food_court()
    if choice == "5":
        cash_register()
    else:
        exit_area(pay)

"""
Permanent options such as show the map and show the shopping list
additional options such as move to other locations
"""
#validated
def exit_area(pay):
    if pay:
        print("Congratulations! you have won the game and successfully survived in the Costco store. You can now go back home and do your homework now.")
        return 0
    else:
        choice = str(input("You can not leave the building until you purchase everything from the shopping list, please select an action you would like to perform \n 1. Check the map \n 2. Check the shopping list \n 3. Show the cart \n 4. Go to the Food court \n"))
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            choice = str(input("Error, the input should be between 1 and 5, please select an action you would like to perform \n 1. Check the map \n 2. Check the shopping list \n 3. Show the cart \n 4. Go to the Food court \n"))
        perm_options(choice)
    if choice == "3":
        cart(cart_list)
        exit_area()
    else:
        food_court()

def display_map():
    output = climage.convert("1.JPG")
    print(output)

def cart(cart_list):
    if len(cart_list) != 0:
        print("In your Cart you have:")
        for i in range(len(cart_list)):
            print(str(i+1) + ". " + cart_list[i])
    else:
        print("your cart is empty")


def leave_item(cart_list):
    cart(cart_list)
    delete = int(input("Please indicate the number beside an item you want to leave: \n"))
    while delete > len(cart_list) or delete < 0:
        delete = int(input("invalid input, Please indicate the number beside an item you want to leave: \n"))
    cart_list.pop(delete-1)

def shopping_list(shoppingList):
    x = 1
    print("Your shopping list:")
    for product in shoppingList:
        print(str(x) + "." + str(product))
        x += 1
    print("")

#validated
def add_item(products):
    print("Available products are: ")
    x = 1
    for product in products:
        print(str(x) + ". " + product)
        x += 1
    choice = int(input("Please indicate which the number beside the product you would like to add to your cart: \n")) - 1
    while choice < 0 or choice > len(products):
        choice = int(input("Invalid input the number has to correspond to one of the products, please indicate which the number beside the product you would like to add to your cart: \n")) - 1
    cart_list.append(products[choice])

def perm_options(choice):
    if choice == "1":
        display_map()
    elif choice == "2":
        shopping_list(shoppingList)


#actual code
print("Welcome to the Ultimate Costco Simulator. Here, you have to get out of Costco store by buying everything from the shopping list that your mom gave you.")
entrance()
