__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''

def smallest_palindrome(word):
    if(word==None):
        return None

    i=0
    j=-1
    k=len(word)

    while(i<k):
        if((word[i]>='a' and word[i]<='z') or (word[i]>='A' and word[i]<='Z')):
            if(word[i].lower()!=word[j].lower()):
                word = word[0:len(word) - i:1] + word[i].lower() + word[len(word)+j+1::1]


                i=i+1
                j=j-1
            else:
                j=j-1
                i=i+1
        else:
            raise ValueError("only letters are allowed")

    return word
    pass

# write your own tests
def test_smallest_palindrome():
    assert "MAdam"==smallest_palindrome("MAd")
    pass
