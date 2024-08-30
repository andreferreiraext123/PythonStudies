# Ask to user which product and how many products be
# And check if the product's name be in the storage

# Storing data
storage = {
    "Tomato": [1000, 2.1],
    "Lettuce": [200, 2.2],
    "Apple": [100, 0.9],
    "Pear": [90, 0.5],
}

total = 0
print("Sales:\n")

while True:
    product = str(input("Enter the product's name:  "))
    if product == "End":
        break
    if product in storage:
        quantity = int(input("Enter the product's quantity: "))
        if quantity < storage[product][0]:
            price = storage[product][1]
            costs = price * quantity
            print(f"{product:12s}: {quantity:6.2f} X {price:6.2f} = {costs:.2f}") # Print each operation
            storage[product][0] -= quantity
            total -= costs
        else:
            print(f"Quantity requered not availlible\n")
            
print(f" Total costs: {total:21.2f}\n")
print("Storage:\n")
for key, data in storage.items():
    print("Description: ", key)
    print("Quantity: ", data[0])
    print(f"Price:{data[1]:6.2f}\n")