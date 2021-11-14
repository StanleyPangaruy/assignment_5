# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

def is_int(n):
    try:
        floatN = float(n)
        intN = int(floatN)
    except ValueError:
        return False
    else:
        return floatN == intN

def is_float(n):
    try:
        floatN = float(n)
    except ValueError:
        return False
    else:
        return True

def lowestNumber():
    num1 = input("First number: ")
    if is_int(num1):
        num1 = int(num1)
    elif is_float(num1):
        num1 = float(num1)
    num2 = input("Second number: ")
    if is_int(num2):
        num2 = int(num2)
    elif is_float(num2):
        num2 = float(num2)
    num3 = input("Third number: ")
    if is_int(num3):
        num3 = int(num3)
    elif is_float(num2):
        num3 = float(num3) 
    if num1 < num2 and num1 < num3:
        print("Lowest Number:",num1)
    elif num2 < num1 and num2 < num3:
        print("Lowest Number:",num2)
    else:
        print("Lowest Number:",num3)

lowestNumber()