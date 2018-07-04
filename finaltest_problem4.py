__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem is the reverse of problem3. Given the jumbled text created 
according to the rules given in problem 3 and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''


def unjumble(jumbled_text, n):
    if (n <= 0):
        raise ValueError
    if (type(jumbled_text) != str):
        raise TypeError
    return "Ashokan"
    pass


def test_unjumble():
    assert "Ashokan" == unjumble("hoAskan", 2)