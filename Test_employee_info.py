import employee_info
print("Test_employee_info")

def test_get_employees_by_age_range():
    input_lower_age_limit = 25
    input_upper_age_limit = 37
    test = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    result = employee_info.get_employees_by_age_range(input_lower_age_limit,input_upper_age_limit)

    assert (result==test)

def test_calculate_average_salary():
    test = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 55000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 65000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 55000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 75000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 65000}
    ]
    calc = (55000+65000+55000+75000+65000+65000)/6
    result = employee_info.calculate_average_salary(test)

    assert (result==calc)