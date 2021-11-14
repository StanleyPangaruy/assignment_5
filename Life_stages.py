# Program 3: Life stages
# Create a program that ask for an age of a person
# Display the life stage of the person.
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

def lifeStage():
    while True:
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Please enter a number.")
            continue
        else:
            break
    if age >= 0 and age <= 12:
        print("Life Stage: Kid")
    elif age >= 13 and age <= 17:
        print("Life Stage: Teen")
    elif age == 18:
        print("Life Stage: Debut")
    else:
        print("Life Stage: Adult")

lifeStage()