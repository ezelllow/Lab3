import price_info

print("Test_price_info")

def test_total_cost_shopping():
    item_list={'apple' : 1, 'orange':2, 'watermelon': 6, 'pineapple': 2, 'pear' : 8, 'papaya': 2, 'pomegranate': 4 }
    test = 81.3

    result = price_info.total_cost_shopping(item_list)

    assert (result == test)

def test_cost_of_fruits():
    fruit = 'apple'
    quantity = 7
    test = 8.4

    result = price_info.cost_of_fruits(fruit, quantity)

    assert (result == test)