# Data input 
Multiplying = int((input("Type a number for multiplication table: ")))
multiplier = 1
multiplier_1 = int(input("Type the last multiplier: "))

# If
while multiplier <= multiplier_1:
    print(f"{Multiplying} X {multiplier} = {(Multiplying * multiplier)}")
    multiplier += 1
