# shopping_cart.py

from pprint import pprint

from datetime import datetime

def to_usd(my_price):  
    return "${0:,.2f}".format(my_price)

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
 ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

##Initializing empty list for user inputs
user_list = []

##Creating "viable" options and converting to string
viable = [p["id"] for p in products]
viable.append("done")
viable = str(viable)

#First user input
user_input = input("Please input a Product ID or type DONE: ").lower()

#If you immediately type DONE, cancel and quit.
if user_input.lower() == "done":
    print("TRANSCATION CANCELLED.")
    quit()

#Check users input against viable options, otherwise append
if user_input not in viable:
    print("ID not recognized. Please try again.")
else:
    user_list.append(user_input)

#Second input. If not viable, get to viable, otherwise append.
while user_input != "done":
    user_input = input("Please input another Product ID or type DONE: ").lower()
    if user_input not in viable:
        print ('ID not recognized. Please try again.')
    else: user_list.append(user_input)
else:
    print("DONE")

#Remove "Done" from list.
user_list.remove('done')

print(user_list)

#####RECEIPT PRINTING SECTION

print("----------------------------------")
print("DIAMOND GROCERIES")
print("WWW.DIAMOND-GROCERIES.EDU")
print("----------------------------------")
print(f"CHECKOUT AT: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("----------------------------------")
print("SELECTED PRODUCTS:")

for items in products:
    # price_usd = to_usd(products[items]['price'])
    # print(f"{products[items]['name']} (${price_usd})")

# for items in user_list:
#     print(items.products['id'])

    # name = " ... "+items.products["name"].title()
    # price = " (${0:.2f})".format(products["price"])
    # print (name+price)


#print(f"{item['name']}...${price_usd}") #You can insert dictionary references in here, too
#     price_usd = to_usd(item['price'])


# print(f"THERE ARE {len(products)} PRODUCTS:")


# item_list.append(user_input)

# print(for p in products 


# for p in products:
#     if p["department"] not in departments:
#         departments.append(p["department"]))