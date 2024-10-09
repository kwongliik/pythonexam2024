# test_string_reverse.py
from question_6_reverse_string import string_reverse  # Replace 'your_module' with the actual module name

def test_string_reverse_empty_string():
    assert string_reverse('') == ''

def test_string_reverse_single_character():
    assert string_reverse('a') == 'a'

def test_string_reverse_multiple_characters():
    assert string_reverse('1234abcd') == 'dcba4321'

def test_string_reverse_mixed_characters():
    assert string_reverse('abc123') == '321cba'

def test_string_reverse_whitespace():
    assert string_reverse('  hello  ') == '  olleh  '
