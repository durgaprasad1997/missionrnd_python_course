__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys
vowels = ('a', 'e', 'i', 'o', 'u')
punctuation = (',', '.')
def to_piglatin(word):
    word=word.lower()
    if word[-1] in punctuation:
        word=word[:-1]
    f=word[0]
    const=''
    n=0
    for c in word:
        if c not in vowels:
            const+=c
            n+=1
        else:
            break
    const+='ay'
    return word[n:]+const

def set(word,res):
    if word[-1] in punctuation:
        res+=word[-1]
    if word[0].isupper():
        res=res[0].upper()+res[1:]
    return res


def pigLatin(text):
    i=text.split()
    res=[]
    for word in i:
        new_word=set(word,to_piglatin(word))
        res.append(new_word)
    return ' '.join(res)


if __name__ == "__main__":
    input=sys.argv[1]
    print(input)
    res=pigLatin(input)
    try:
        while True:
            print(res)
    except KeyboardInterrupt:
        pass

    pass
    #sys.exit(main())