import employee_info as EMP
from employee_info import employee_data as EMPDATA


def test_get_employees_by_age_range():
    upper = 33
    lower = 29
    expected = [EMPDATA[0], EMPDATA[4]]
    result = EMP.get_employees_by_age_range(lower, upper)
    assert(result == expected)


def test_calculate_average_salary():
    expected = 60166.67 # Rounded to 2 decimal points
    result = EMP.calculate_average_salary()
    assert(result == expected)


def test_get_employees_by_dept_engg():
    targetDept = "Engineering"
    expected = [EMPDATA[3], EMPDATA[4]]
    result = EMP.get_employees_by_dept(targetDept)
    assert(result == expected)


def test_get_employees_by_dept_marketing():
    targetDept = "Marketing"
    expected = [EMPDATA[1], EMPDATA[2]]
    result = EMP.get_employees_by_dept(targetDept)
    assert(result == expected)


