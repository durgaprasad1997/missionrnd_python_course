__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.
 With in an anagram group, order them in case insensitive ascending sorting order.
 If 2 anagram groups have same count, then set with smaller starting word comes first.
 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.
 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.
 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys

import unit6utils
import string

def are_anagrams(first, second):
    if first is None or second is None: return False
    word1 = list(first.lower())
    word2 = list(second.lower())
    for c in word1:
        if c not in word2: return False
        word2.remove(c)
    return True

def anagram_sort(source, destination):
    f = open(source, 'r')
    words = []
    for line in f:
        if len(line) <= 1 or line.split()[0] == '#': continue
        words.extend(line.split())
    anagram_groups = []
    processed_words = []
    for i in range(len(words)):
        word = words[i]
        if word in processed_words: continue
        anagram_group = (word,)
        processed_words.append(word)
        for j in range(i+1,len(words)):
            if are_anagrams(word,words[j]):
                anagram_group += (words[j],)
                processed_words.append(words[j])
        if len(anagram_group) > 0:
            anagram_group = sorted(anagram_group, key=lambda s: s.lower())
            anagram_groups.append(anagram_group)
    anagram_groups = sorted(anagram_groups, key=lambda lst: lst[0].lower())
    anagram_groups = sorted(anagram_groups, key=lambda lst: (len(lst)), reverse=True)
    f.close()
    f = open(destination,'w')
    output = ""
    for group in anagram_groups:
        output += '\n'.join(group)
        output += '\n'
    f.write(output)
    f.close()

if __name__ == "__main__":
    fin = sys.argv[1]
    fout = fin[:fin.find('.txt')] + "-results.txt"

    try:
        source = unit6utils.get_input_file(fin)
        destination = unit6utils.get_input_file(fout)
        anagram_sort(source, destination)
    except:
        print ("Some error occured! Try again.")
    else: print ('Completed successfully.')
    #sys.exit(main())