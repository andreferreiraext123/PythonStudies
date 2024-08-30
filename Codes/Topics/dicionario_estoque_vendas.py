# Storing data

storage = {
    "Tomato":   [1000, 2.30],
    "Lettuce":  [500, 0.45],
    "Potato":   [2001, 1.20],
    "Beans":    [100, 1.50]
}

sale = [["Tomato", 5], ["Potato", 10], ["Lettuce", 5]]
total = 0

print("Sales:")
for operation in sale: 
    product, quantity = operation # Product index 0, quantity index 1 from element in (sale) list

    price = storage[product][1] # Access dicionary and access pruduct-key on index 1 that is the price the second parameter from keys in storage dicionary
    cost = price * quantity
    print(f"{product:12s}:  {quantity:2d} X {price:6.2f} = {cost:6.2f}")
    storage[product][0] -= quantity # Access the key in storage by parameter product, after access the index 0 on the key
    total += cost # Storing the costs from each operation

print(f"Total costs: {total:21.2f}\n")
print(f"Storage:    \n")
for key, data in storage.items(): # Key is the parameter from the keys in dictionary in storage, and data is the represents the data from the keys (Tuples)
    print(f"Description:",key) # Print key
    print(f"Quantity:",data[0]) # Print quantity
    print(f"Price:{data[1]:6.2f}\n") # Print price
print(storage)