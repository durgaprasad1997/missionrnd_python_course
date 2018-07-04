__author__ = 'Kalyan'

max_marks = 25  # encrypt -> 13, decrypt 12

problem_notes = '''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''

# do type checking, non-str should raise TypeException
def encrypt(text, key):
    if type(text)!=str or type(key)!=str:
        raise TypeError
    if(len(key)==0 or key.isalpha()==False):
        raise ValueError

    key=key*5
    j=0
    k=0
    t=text
    for i in text:
        if(i!=" "):
            t=t[:j-1]+chr(ord(i)+ord(key[k])-97)+t[j+1:len(t)]
            k+=1
            #t=t.replace(i,chr(ord(i)+ord(key[j])-97))
            print(t)
        j+=1


    print(t)
    pass

def decrypt(text, key):
    pass


def test_encrypt():
    assert "hj vkirf" == encrypt("hi there", "abcde")

def test_decrypt():
    assert "hi there" == decrypt("hj vkirf", "abcde")

