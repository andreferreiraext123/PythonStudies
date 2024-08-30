dicionary = {
    "Andre": 30,
}

value = dicionary.get("Andre1")
print(value) # Output: None

value_1 = dicionary.get("Andre1", "Value not found!")
print(value_1) # Output: Value not found
