max_marks = 20

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, then order them lexicographically (case insensitive). For e.g. a comes before b

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.


Note: 
1. use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
2. You can write additional routines as you see fit.
'''

def transform(sentence):

    if(type(sentence) != str ):
        raise TypeError
    for z in sentence.split(" "):
        if(z.isalpha()==False):
            raise ValueError

    x=sentence.split(" ")
    c=0
    for j in x:
        if j=="":
            del x[c]
            c-=1
        c+=1
    y=x

    x.sort(reverse=True,key=len)

    for i in x:
        for j in x:
            if len(i)==len(j):
                if sum(ch in 'aeiou' for ch in i)<sum(ch in 'aeiou' for ch in j):
                    x[x.index(i)],x[x.index(j)]=j,i
                if sum(ch in 'aeiou' for ch in i)==sum(ch in 'aeiou' for ch in j):
                    i.lower()
                    j.lower()
                    if i>j:
                        x[x.index(i)], x[x.index(j)] = j, i

    #x=sorted(x,key = lambda word: sum(ch in 'aeiou' for ch in word),reverse = True)

    s=""
    for i in x:
        s=s+i+" "
    s=s[:-1]
    print(s)
    print(len(s))
    return s
    pass


def test_transform():
    assert "elephant walking runway on" == transform("walking elephant on runway")