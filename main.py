import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students = pd.read_csv("students_100.csv")
subjects = ["python" , "sql" , "html" , "css" , "javascript"]
#calculate total , average and percentage
students["total_marks"] = students[subjects].sum(axis=1)
students["average"] = students[subjects].mean(axis = 1)
students["percentage"] = (students["total_marks"]/500)*100

def assign_grades(percentage):
    if percentage>=90:
        return "A"
    elif percentage >=80:
        return "B"
    elif percentage >=70:
        return "C"
    elif percentage >=60:
        return "D"
    elif percentage >=50:
        return "E"
    else:
        return "F"

def result_assign(marks):
    if any(mark < 35 for mark in marks):
        return "Fail"
    return "Pass"

students["grade"] = students["percentage"].apply(assign_grades)
students["results"] = students.apply(lambda row : result_assign(row[subjects].tolist()) , axis=1)
print(students)

print("Total students : " , len(students))
print("Class Average : " , round(students["average"].mean(),2))
topper = students.loc[students["average"].idxmax()]
print("Topper Name : ", topper["name"])
print("Topper Average : ",topper["average"])
print("Number of pass students : ",(students["results"]=="Pass").sum())
print("Number of fail students : ",(students["results"] == "Fail").sum())
print("subject wise Average : ")
print(round(students[subjects].mean(),2))

print("Top 3 students are :")
print(students.sort_values(by="percentage" , ascending=False).head(3))
