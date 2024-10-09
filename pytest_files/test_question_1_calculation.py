import pytest
from question_1_calculation import *
#import isipadu_tangki_air

def test_calculation():
    # Test case 1: Normal case
    a, b = 30, 5
    result = calculation(a, b)
    expected = (a - b, a * b, a / b)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 2: Case with a zero (to test division)
    a, b = 10, 2
    result = calculation(a, b)
    expected = (a - b, a * b, a / b)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 3: Case with negatives
    a, b = -4, 6
    result = calculation(a, b)
    expected = (a - b, a * b, a / b)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 4: Case where division could return a float
    a, b = 7, 3
    result = calculation(a, b)
    expected = (a - b, a * b, a / b)
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test case 5: Case where 'b' is zero (to handle division by zero)
    a, b = 10, 0
    with pytest.raises(ZeroDivisionError):
        calculation(a, b)

def test_main(capfd):
    # Call the main function
    main()

    # Capture printed output
    captured = capfd.readouterr()

    # Define expected output
    expected_output = "subtraction = 25, multiplication = 150, division = 6.0\n"

    # Assert that the captured output matches the expected output
    assert captured.out == expected_output, f"Expected {expected_output}, but got {captured.out}"
