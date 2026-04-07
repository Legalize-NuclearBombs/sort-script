from reports.coffee import MedianCoffee


def test_median_coffee_calculation():
    report = MedianCoffee()
    test_data = [
        {'student': 'Alice', 'coffee_spent': '100'},
        {'student': 'Alice', 'coffee_spent': '200'},
        {'student': 'Alice', 'coffee_spent': '300'},
        {'student': 'Bob', 'coffee_spent': '50'},
        {'student': 'Bob', 'coffee_spent': '400'},
        {'student': 'Bob', 'coffee_spent': '100'},
    ]

    result = report.calculate(test_data)

    assert result[0] == ['Alice', 200.0]
    assert result[1] == ['Bob', 100.0]
    assert result[0][1] > result[1][1]
