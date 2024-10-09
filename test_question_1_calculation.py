# test_calculation.py

from question_1_calculation import calculation

def test_calculation():
    # Test case 1
    result = calculation(40, 10)
    assert result == (30, 400, 4), "Test case 1 failed"

    # Test case 2
    result = calculation(20, 5)
    assert result == (15, 100, 4), "Test case 2 failed"

    # Test case 3
    result = calculation(50, 5)
    assert result == (45, 250, 10), "Test case 3 failed"