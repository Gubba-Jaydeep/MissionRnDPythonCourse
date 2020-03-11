__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Return the n most frequently occurring chars and their respective counts
e.g cccaaaaabbbb, 2 should return [(a 5) (b 4)]
in case of a tie, return char which comes earlier in alphabet ordering (capitals before smalls)
e.g. cdbba,2 -> [(b,2) (a,1)]
use standard types and and builtin functions we have used in the course.

constraints:
1. raise TypeError if word is not a str or n is not an int
2. raise ValueError if n <= 0,
3. if n > number of unique chars return the available chars and 
   their counts (sorted by above criteria)
4. The function should be case sensitive (ie) A and a are different. 
   So aaAABBB, 2 should return [(B,3), (A,2)]
'''

def most_frequent(word, n):
    pass


#write your own tests.
def test_most_frequent():
    assert [('a',5),('b',4)] == most_frequent("aaaaabbbbcccdde", 2)