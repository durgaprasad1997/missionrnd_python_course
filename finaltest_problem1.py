__author__ = 'Kalyan'

max_marks = 20

from operator import itemgetter

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''
def get_all_substrings(string):

  length = len(string)
  alist = []
  for i in range(length):
    for j in range(i,length):
      alist.append(string[i:j + 1])

  #print(alist)
  return alist


def repeats(digits):
    if type(digits) != str:
        raise TypeError
    ot=[]

    l=get_all_substrings(digits)
    for i in l:
        if i in digits and len(i)>=2 and digits.count(i)>=2:
            ot.append([i,digits.count(i)])

    #print(ot)

    l=ot

    k=0
    for i in l:
        l[k]=tuple(l[k])
        k+=1

    l=set(l)
    l=list(l)
    l.sort(key=lambda x: x[1], reverse=True)
    #print(l)


    i=0

    x=len(l)
    while(i<x):
        j=i+1

        while(j<x):

            print(i,j)
            p=i
            q=j
            if(l[p][1]==l[q][1] and int(l[p][0])<int(l[q][0])):
                #print(i,j)
                x1,y=l.index(l[p]),l.index(l[q])
                l[x1],l[y]=l[y],l[x1]
            j += 1
        i+=1




    print(l)
    return l

    pass


def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")