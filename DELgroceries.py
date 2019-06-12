# groceries.py

# from pprint import pprint

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

#pprint(products)

print ('--------------')
print('THERE ARE '+str(len(products))+' PRODUCTS:')
print ('--------------')

for prod in products:
    name = "+ "+prod["name"].title()
    price = " (${0:.2f})".format(prod["price"])
    print (name+price)

######################################################################

departments = []

for p in products:
    if p["department"] not in departments:
        departments.append(p["department"])

dept_count = len(departments)

unique_departments = list(set(departments))

print ('--------------')
print('THERE ARE ' +str(dept_count) +' DEPARTMENTS:')
print ('--------------')

unique_departments.sort()

for d in unique_departments:
    totalprod = [p for p in products if p["department"] == d]
        #Return P(P1) for every P (P2) in Products if P (P3) has same name as department
        #For each item in our list of products, return that item if its
        #department equals the department name we are looking at (d in for d)
    totalprodcount = str(len(totalprod))
    print(" + "+
    d.title()
    +" ("
    + totalprodcount
    +" products)"
    )


print(
    [p for p in products if p["department"] == "snacks"] # RETURNING ALL PRODUCTS IN SNACKS
    )
print(
    [p["name"] for p in products if p["department"] == "snacks"] # RETURNING ALL NAMES IN SNACKS
    )
#breakpoint()
# # # # breakpoint() - THIS WILL ALLOW YOU TO DEBUG/WORK DIRECTLY IN SCRIPT FROM TERMINAL
# #STRING INTERPOLATION
# print(f"THERE ARE {len(products)} PRODUCTS:")
# print(f"THERE ARE {dept_count} DEPARTMENTS:")

# for item in products:
#     price_usd = to_usd(item['price'])

#     print(f"{item['name']}...${price_usd}") #You can insert dictionary references in here, too


##################################################
##################################################
##################################################

# for d in unique_departments:
#     print(d.title())








#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

# print ('--------------')
# print('THERE ARE '+str(len(products))+' PRODUCTS:')
# print ('--------------')

# for i in range(0,len(products)):
#     print(' + '
#     +products[i]['name']
#     +' ($'
#     +str(format(products[i]['price'],'.2f')) #Convert to string, format 2 decimals
#     +')')


# for i in range(0,len(products)):

# #List of Departments
# deptlist = products[i]['department'].capitalize()

# #Filter unique departments
# def uniquedep(department):
#     possible = ['Snacks', 'Pantry', 'Beverages', 'Frozen', 'Personal care', 'Dairy eggs', 'Household', 'Babies', 'Meat seafood', 'Dry goods pasta']
# if department in possible:
#         return True
#     else:
#         return False

# print ('--------------')
# print('THERE ARE '+str(len(products))+' PRODUCTS:')
# print ('--------------')

# for prod in products:
#     name = "+ "+prod["name"].capitalize()
#     price = (" ($"
#         +str(
#             format(prod["price"],'.2f')
#             )
#         +')')
#     print (name+price)


