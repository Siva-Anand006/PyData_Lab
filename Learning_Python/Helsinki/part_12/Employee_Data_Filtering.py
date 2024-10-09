employees = [
    ("John Doe", 34, 55000, "Engineering"),
    ("Jane Smith", 28, 48000, "Marketing"),
    ("Sam Wilson", 45, 68000, "HR"),
    ("Mary Johnson", 40, 75000, "Engineering"),
    ("Linda Brown", 38, 72000, "Sales"),
    ("Tom Clark", 29, 50000, "Marketing")
]


def age_over_30(employee):
    return employee[1] > 30

def salary_above_60000(employee):
    return employee[2] > 60000

def department_engineering(employee):
    return employee[3] == "Engineering"

def filter_employees(employees : list, criteria : list):
    return [employee for employee in employees if all(criterion(employee) for criterion in criteria) ]

criteria = [age_over_30, salary_above_60000, department_engineering]
filtered_employees = filter_employees(employees, criteria)

print(filtered_employees)
