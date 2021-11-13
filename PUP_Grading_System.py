# Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

import math

#step 1: get their grades
def getGrade():
    grade_ = float(input("Grade percentage: "))
    return grade_

#function that rounds up/down number the traditional way 
def normalRound(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

gradeF = getGrade()
grade = normalRound(gradeF)




