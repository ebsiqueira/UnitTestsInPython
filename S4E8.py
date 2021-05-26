def calculate_tax(amount, tax_rate, age):
    """The function returns the amount of income tax."""

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))

# enter your solution here
def test_calculate_tax():
    assert calculate_tax(60000, 0.15, 10) == 5000
    assert calculate_tax(60000, 0.15, 18) == 5000
    assert calculate_tax(60000, 0.15, 19) == 9000
    assert calculate_tax(60000, 0.15, 65) == 9000
    assert calculate_tax(60000, 0.15, 66) == 8000

test_calculate_tax()