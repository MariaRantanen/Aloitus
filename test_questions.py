# questions.py tests can be found here
# ------------------------------------

import questions

# Test if conversion to integer works as expected
# def test_ask_user_integer(monkeypatch): # Simulate user input using Monkeypathc library
#     user_input = '100'
#     monkeypatch.setattr('builtins.input', lambda _: user_input) # Use anonymous function to create input from variable
#     question = questions.Question('Anna kokonaisluku')
#     assert question.ask_user_integer(False) == (100, 'OK', 0, 'Conversion successful')

# # Test an error condition when user adds a unit to a number
# def test_ask_user_integer2(monkeypatch):
#     user_input = '100 v'
#     monkeypatch.setattr('builtins.input', lambda _: user_input) # korvataan järjestelmän input() muuttujalla syote
#     question = questions.Question('Anna kokonaisluku')
#     assert question.ask_user_integer(False) == (0, 'Error', 1, "invalid literal for int() with base 10: '100 v'")

# Test static conversion method to integer


def test_static_ask_user_integer(monkeypatch):
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_integer(
        'Anna kokonaisluku', False) == (100, 'OK', 0, 'Conversion successful')

# Test if conversion to float works as expected


# Simulate user input using Monkeypathc library
def test_ask_user_float(monkeypatch):
    user_input = '1.5'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_float("Anna liukuluku: ", False) == (
        1.5, 'OK', 0, 'Conversion successful')

# Test an error condition when user adds a unit to a floating point number


# Simulate user input using Monkeypathc library
def test_ask_user_float2(monkeypatch):
    user_input = '1.5v'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_float("Anna kokonaisluku", False) == (
        0, 'Error', 1, "could not convert string to float: '1.5v'")


# Simulate user input using Monkeypathc library
def test_ask_user_boolean(monkeypatch):
    user_input = 'y'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_boolean("Haluatko jatkaa", 'Y', 'N', False) == (
        True, 'OK', 0, 'Conversion successful')

# Test conversion to boolean: case N


# Simulate user input using Monkeypathc library
def test_ask_user_boolean2(monkeypatch):
    user_input = 'n'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_boolean("Haluatko jatkaa", 'Y', 'N', False) == (
        False, 'OK', 0, 'Conversion successful')

# Test an error condition


# Simulate user input using Monkeypathc library
def test_ask_user_boolean3(monkeypatch):
    user_input = 'v'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_boolean("Haluatko jatkaa", 'Y', 'N', False) == (
        'N/A', 'Error', 1, 'unable to convert to boolean')
    
# Test to get value from dictionary
def test_ask_user_dictionary(monkeypatch):
    user_input = "tyttö"
    gender_dictionary = {"tyttö": 0, "poika": 1}
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_dictionary("Sukupuoli: ", gender_dictionary, False) == (0, "OK", 0, "Conversion successful")

# Test to get eroor when is missing
def test_ask_user_dictionary2(monkeypatch):
    user_input = "jätkä"
    gender_dictionary = {"tyttö": 0, "poika": 1}
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_dictionary("Sukupuoli: ", gender_dictionary, False) == ('N/A', 'Error', 1, "'jätkä'")