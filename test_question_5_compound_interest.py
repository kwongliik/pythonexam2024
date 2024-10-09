# test_compound_interest.py
from question_5_compound_interest import compound_interest, calculate_and_print_matured_value

def test_compound_interest():
    assert compound_interest(1000, 5, 2, 1) == 1102.50
    assert compound_interest(1500, 3.5, 3, 4) == 1665.3051756777352
    assert compound_interest(2000, 7, 5, 12) == 2835.2505192279805

def test_calculate_and_print_matured_value(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["10000", "4.5", "6", "4"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    calculate_and_print_matured_value()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Matured value is 13079.91"
