students = [
    ("Alice", 21, 85, "New York"),
    ("Bob", 20, 92, "Los Angeles"),
    ("Charlie", 22, 78, "Chicago"),
    ("Diana", 23, 88, "New York"),
    ("Eve", 20, 95, "Los Angeles")
]


def age_above_20(student):
    return student[1] > 20

def grade_above_80(student):
    return student[2] > 80

def multi_criteria_filter( students, criteria : list):
    return [ student for student in students if all(criterion(student) for criterion in criteria) ]
    
criteria = [age_above_20, grade_above_80]
filtered_students = multi_criteria_filter(students, criteria)
print(filtered_students)


