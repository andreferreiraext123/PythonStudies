def division():
    while True:
        try:
            num_1 = int(input("Enter the first number: "))
            num_2 = int(input("Enter the second number: "))
            if num_2 == 0:
                raise ZeroDivisionError("You can't divide by zero")
            result = num_1 / num_2
        except ValueError:
            print("Just integer numbers")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"Something is wrong: {e}")
        else:
            print(f"The result is: {result}")
            break
        finally:
            print("Attempt finally!")
division()
