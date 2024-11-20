import price_info as PI


def test_cost_of_fruit():
    fruitname = "pear"   # price is $0.90
    quantity = 5
    expected = 4.50
    result = PI.cost_of_fruits(fruitname, quantity)
    assert(result == expected)


def test_total_cost():
    PI.quantity_list = {'apple': 5, 'orange':5, 'watermelon': 2, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
    expected = 46.75 + 6.50   # +6.50 because of extra one watermelon to purchase, priced at $6.50
    result = PI.total_cost_shopping()
    assert(result == expected)