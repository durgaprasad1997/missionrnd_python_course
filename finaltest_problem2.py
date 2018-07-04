__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Imagine a line starting from 0 to infinity.

You color parts of that line green by specifying it as an interval. For e.g  (0, 2) will cover the segment from 0 to 2 
green.

You are given a list of tuples that have to be colored green. If the tuples are overlapping 
and part of the line is already green, the uncolored part is colored green.

For e.g. if input is (20, 21) (5,11) and (45, 47) then effectively 9 units will be colored green.

Your job is to figure out how much length of the line has been colored green if these tuples are applied.

Notes:
1. No type checking required, assume low and high are ints > 0. Assume you are given a valid list of tuples
2. The intervals can be long, so you must not timeout for large values.

'''

def get_green_length(segments):

    count=0
    for i in segments:
        count+=i[1]-i[0]
    print(count)
    x=len(segments)
    s=set()
    for i in segments:
        s.update(range(i[0],i[1]+1))

    print(s)






    return len(s)-len(segments)
    pass


def test_get_green_length():
    assert 15 == get_green_length([(20,21), (5,11), (12,20)])