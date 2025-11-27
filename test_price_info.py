import price_info as price


def test_total_cost_shopping():
    map={'apple':10,'orange':10}
    price.quantity_list=map
    expected=26

    total_cost=price.total_cost_shopping()

    assert(total_cost==expected)
    





def test_cost_of_fruit():
    expected=12

    price_fruits=price.cost_of_fruits('apple', 10)

    assert(price_fruits==expected)
