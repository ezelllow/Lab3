import Lab2.Lab2 as Lab2
print("Test_Lab2")

def test_find_min_max():
    result = []
    input_arr = [1,2,3,4,5]
    test_arr = [1, 5]

    result = Lab2.calc_min_max_temperature(input_arr)

    assert (result == test_arr)
   
def test_calc_average_temperature():
    result = []
    input_arr = [2,6]

    result = Lab2.calc_average_temperature(input_arr)

    assert (result == 4.0)

def test_calc_median_temperature():
    result = []
    input_arr = [1,2,3,4,5]

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == 3)