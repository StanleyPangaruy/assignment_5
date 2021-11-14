# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

#This module provides access to the mathematical functions
import math

#function that rounds up/down number the common method
def normalRound(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

#main funciton for getting the entered grade and 
#displaying its equivalent grade/mark and description
def gradingSystem():
    gradeInput = float(input("Grade percentage: "))
    grade = normalRound(gradeInput)
    if grade >= 97 and grade <= 100:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 1.0")
        print("Description: Excellent")
    elif grade >= 94 and grade <= 96:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    elif grade >= 91 and grade <= 93:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 1.5")
        print("Description: Very Good")
    elif grade >= 88 and grade <= 90:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 1.75")
        print("Description: Very Good")
    elif grade >= 85 and grade <= 87:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 2.0")
        print("Description: Good")
    elif grade >= 82 and grade <= 84:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 2.25")
        print("Description: Good")
    elif grade >= 79 and grade <= 81:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 2.5")
        print("Description: Satifactory")
    elif grade >= 76 and grade <= 78:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 2.75")
        print("Description: Satisfactory")
    elif grade == 75:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 3.0")
        print("Description: Passing")
    elif grade >= 65 and grade <= 74:
        print("Input Grade: ", gradeInput)
        print("Grade/Mark: 5.0")
        print("Description: Failure")

gradingSystem()





