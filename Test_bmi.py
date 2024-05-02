import Lab2.bmi as bmi
def test_bmi_normal_weight():
    result = []
    height = 1.73
    weight = 57
    result = bmi.calculate(height,weight)
    assert result==0
def test_bmi_over_weight():
    result = []
    height = 1.73
    weight = 87
    result = bmi.calculate_bmi(height,weight)
    assert result==1
def test_bmi_under_weight():
    result = []
    height = 1.73
    weight = 47
    result = bmi.calculate_bmi(height,weight)
    assert result==-1
