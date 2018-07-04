__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].






def base10to5(num, base):

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string


def to_custom_base5(number):
    if(type(number).__name__!='int'):
        raise TypeError("only int")
    number=int(base10to5(number,5))
    d={0:'a',1:'e',2:'i',3:'o',4:'u'}
    s=""
    """ if(number<0):
        number=number*-1
        s=s+'-'"""

    while(number>0):
        x=number%10
        s=s+d[x]
        number=int(number/10)

    s=s[::-1]
    print(s)
    return s

    pass

# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.
def from_custom_base5(s):
    dd = {'a':0, 'e':1,'i':2,'o':3, 'u':4}

    i=0
    x=0
    while(i<len(s)):
        x=x*5+dd[s[i]]
        i=i+1




    return x

    pass

# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "ia" == to_custom_base5(10)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("ia")