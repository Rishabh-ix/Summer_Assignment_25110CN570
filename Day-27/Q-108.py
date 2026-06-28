# Marksheet Generation System Program.

print("===== Marksheet Generation System =====")

roll = int(input("Enter Roll Number: "))
name = input("Enter Student Name: ")

english = float(input("Enter English Marks: "))
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
computer = float(input("Enter Computer Marks: "))
hindi = float(input("Enter Hindi Marks: "))

total = english + maths + science + computer + hindi

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n========== MARKSHEET ==========")
print("Roll Number :", roll)
print("Student Name:", name)

print("\nMarks")
print("English :", english)
print("Maths :", maths)
print("Science :", science)
print("Computer :", computer)
print("Hindi :", hindi)

print("\nTotal Marks :", total, "/500")
print("Percentage :", percentage, "%")
print("Grade :", grade)
print("===============================")