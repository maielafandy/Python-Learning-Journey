students = [
    {'Name': "ali", 'grade': 90},
    {'Name': "sara", 'grade': 95},
    {'Name': "Omar", 'grade': 80},
    {'Name': "Mai", 'grade': 100}
]

print("------------------------------------") 

for index, student in enumerate(students):
    print(f"{index+1}-{student['Name']}")
print("------------------------------------")
for index, student in enumerate(students):
    print(f"{index+1}-{student['grade']}")
print("------------------------------------")
for index, student in enumerate(students):
    print(f"{index+1}-{student['Name']} -> {student['grade']} ")
print("------------------------------------")


highest = students[0]['grade']

for student in students:
    if student['grade'] > highest:
        highist = student['grade']
        best_student = student['Name']


print(f"Best student is {best_student} \ngrade is {highist}")
