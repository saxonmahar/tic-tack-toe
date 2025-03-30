#define the menu of restaurant
menu = {
    "Burger": 3.99, 
    "sandwich": 5.99,
    "Fries": 1.29,
  "Soda": 0.99,
    "Milkshake": 1.89
}
# print the menu
print("Welcome to the restaurant")
print("Menu:")
for item in menu:
    print(item, ":", menu[item]) 
# take the order from the user
order = input("Enter your order: menu: ")
# check if the order is in the menu
if order in menu:
    print("Thank you for your order")       
else :
    print("Sorry, we don't have that item")
    another = input("Would you like to order another item? (y/n): ")
    if another == "y":
        order = input("Enter your order: ")
    else:
        print("Thank you for your order")
# calculate the total price
total = 0
for item in order.split(","):
    total += menu[item]
print("Your total is: ", total)
# take the payment from the user
payment = float(input("Enter your payment: "))
if payment < total:
    print("Sorry, that's not enough")
    payment = float(input("Enter your payment: "))
else:
    print("Thank you for your payment") 
# calculate the change
change = payment - total            
print("Your change is: ", change)
print("Thank you for your order. Have a nice day!") # Take the order from the user
order = input("Enter your order (comma-separated for multiple items): ").split(",")
valid_order = []
invalid_items = []

# Validate each item
for item in order:
    item = item.strip()  # Remove extra spaces
    if item in menu:
        valid_order.append(item)
    else:
        invalid_items.append(item)

# Inform the user about invalid items
if invalid_items:
    print("Sorry, we don't have the following items:", ", ".join(invalid_items))

# Calculate the total price for valid items
total = 0
for item in valid_order:
    total += menu[item]

if valid_order:
    print("Your valid order:", ", ".join(valid_order))
    print("Your total is: $", total)
else:
    print("No valid items in your order.")    # Take the order from the user
    order = input("Enter your order (comma-separated for multiple items): ").split(",")
    valid_order = []
    invalid_items = []
    
    # Validate each item
    for item in order:
        item = item.strip()  # Remove extra spaces
        if item in menu:
            valid_order.append(item)
        else:
            invalid_items.append(item)
    
    # Inform the user about invalid items
    if invalid_items:
        print("Sorry, we don't have the following items:", ", ".join(invalid_items))
    
    # Calculate the total price for valid items
    total = 0
    for item in valid_order:
        total += menu[item]
    
    if valid_order:
        print("Your valid order:", ", ".join(valid_order))
        print("Your total is: $", total)
    else:
        print("No valid items in your order.")        # Take the order from the user
        order = input("Enter your order (comma-separated for multiple items): ").split(",")
        valid_order = []
        invalid_items = []
        
        # Validate each item
        for item in order:
            item = item.strip()  # Remove extra spaces
            if item in menu:
                valid_order.append(item)
            else:
                invalid_items.append(item)
        
        # Inform the user about invalid items
        if invalid_items:
            print("Sorry, we don't have the following items:", ", ".join(invalid_items))
        
        # Calculate the total price for valid items
        total = 0
        for item in valid_order:
            total += menu[item]
        
        if valid_order:
            print("Your valid order:", ", ".join(valid_order))
            print("Your total is: $", total)
        else:
            print("No valid items in your order.")