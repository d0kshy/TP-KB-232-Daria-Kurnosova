students = [
    {'name': 'Daria', 'grade': 88},
    {'name': 'Andrii', 'grade': 78},
    {'name': 'Pavlo', 'grade': 92},
    {'name': 'Mykyta', 'grade': 64},
]

sorted_by_name = sorted(students, key=lambda student: student['name'])
sorted_by_grade = sorted(students, key=lambda student: student['grade'])

print(f"\nList was sorted by name: {sorted_by_name}.")
print(f"List was sorted by grade: {sorted_by_grade}.\n")