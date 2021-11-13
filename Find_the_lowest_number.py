# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

def lowestNumber():
    num1_ = int(input("First number: "))
    num2_ = int(input("Second number: "))
    num3_ = int(input("Third number: "))
    if num1_ < num2_ and num1_ < num3_:
        print(num1_)
    elif num2_ < num1_ and num2_ < num3_:
        print(num2_)
    else:
        print(num3_)

lowestNumber()
