import employee_info as info


def test_get_employees_by_age_range():
    expected = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
   
]
    result=info.get_employees_by_age_range(20,30)

    assert(expected==result)



def test_calculate_average_salary():
    expected=60166.67

    result=info.calculate_average_salary()

    assert(expected==result)

def test_get_employees_by_dept():
    expected = [
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]

    result=info.get_employees_by_dept('Engineering')

    assert(expected==result)