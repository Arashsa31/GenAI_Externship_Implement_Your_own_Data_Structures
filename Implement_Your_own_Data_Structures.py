print("Welcome to the Inventory Manager!")

#Step 1: Create the Inventory
inventory = {
"apple": (10, 2.5),
"banana": (20, 1.2)
}

#Step 2: Add, Remove, and Update Items
inventory["mango"] = (15, 3.0)
if "mango" in inventory:
    del inventory["mango"]
inventory["mango"] = (15, 3.0)
if "mango" in inventory:
    inventory["mango"] = (10, 3.5)

#Step 3: Display the Inventory
print("Current inventory:")
for item, (quantity, price) in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

#Step 4: Bonus - Calculate Total Value
total_value = 0
for quantity, price in inventory.values():
    total_value += quantity * price
print(f"Total value of inventory: ${total_value:.1f}")