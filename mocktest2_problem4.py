__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
You're given a text file containing names of movie actors and films they've acted in - delimited
by : after actor and movies are separated by commas as described below. movie names may contain : and space
too but not a comma.

Format:
{actor name}: {movie name 1}, {movie name 2}, {movie name 3}

Input:
File containing movies info, a number 'n' which represents the number of lines from top of file and a list 
of movies that I like.  n is used to simulate various files instead of having different movies files for testing.

Output:
The top k actors that I might like based on the movies given. The actors are sorted by the number of movies 
they acted in (descending). In case of a tie, sort by name (insensitive)

Example:
I like movies m1, m2, m3 and the actors who acted in them (in the first N lines) are as follows
m1 : a1, a3, a5 
m2 : a2, a3
m3:  a2, a3, a6

Then top 2 actors that I might like are a3 and a2.

Notes:
1. No special type checking required. raise ValueError if n < 0. 
2. You must work as if the file has only n lines.
3. See if you can decompose this problem into meaningful subroutines.
4. If a movie that is given do not exist in the top N lines, then ignore that movie (as if no one acted in it)
5. The movies must be treated in a case insensitive manner (ie) Inception and inception refer to the same movie. 
6. The actors returned must be in the same case as given in the input file (Tom Hardy and not tom hardy).   

UPLOAD THE movies.txt file into your drive folder as well ** Do not modify the movies.txt file! **

'''

import inspect
import os


# returns the top k actors sorted by the specified criteria.
# It is as if the file has only first n lines.
# Important: Use the helper routine given (open_input_file) to open the file to open the file which should
# be in same directory as this file.
def get_favorite_actors(input_file, n, movies, k):
    l=[]
    f=open_input_file(input_file)
    for i in range(n):
        l1=[]
        s=f.readline()
        for j in movies:
            if j in s:
                l1.append(s.split(":")[0])

        l.append(l1)

    print(l)


    f.close()
    
    pass


def test_get_favorite_actors():
    assert ['Leonardo Di Caprio', 'Tom Hardy'] == get_favorite_actors("movies.txt", 4, ["Inception"], 2)


def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)


def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


