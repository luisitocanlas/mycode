# basic calculator

try:
    num = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"{num} / {num2} = {num / num2}")

# let's add handling for SPECIFIC types of errors!
except ZeroDivisionError:
    print("You can't divide by zero, dummy!")

except ValueError:
    print("You can only type in NUMERALS, dummy!")

# you want Python to save the error message as an obj
except Exception as somevarwakkawakka:
    print("There was an error!", somevarwakkawakka)

# this is optional
finally:
    print("This runs no matter what!")