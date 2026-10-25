name = input("Enter student name: ")
print("Student Name:", name)

maths = int(input("Enter Maths marks: "))
english = int(input("Enter English marks: "))
hindi = int(input("Enter Hindi marks: "))

total = maths + english + hindi
print("Total Marks:", total)

percentage = (total / 300) * 100
print("Percentage:", percentage)

if maths >= 33 and english >= 33 and hindi >= 33:
    print("Pass")
else:
    print("Fail")
