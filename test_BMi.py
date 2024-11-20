import DOAIOT_Lab2.bmi as bmi

def test_calculate_bmi_underweight():
    expected = -1
    result = bmi.calculate_bmi(weight="27", height="1.73")
    assert result == expected

def test_calculate_bmi_overweight():
    expected = 1
    result = bmi.calculate_bmi(weight="77", height="1.73")
    assert result == expected

def test_calculate_bmi_normal():
    expected = 0
    result = bmi.calculate_bmi(weight="57", height="1.73")
    assert result == expected