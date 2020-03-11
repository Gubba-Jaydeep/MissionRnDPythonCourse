__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
This is a simple text transformation problem. 

Some definitions:

Mirror:
We define mirror of a letter as the corresponding letter from the end in the alphabet. For e.g. 'z' is mirror of 'a', 
'y' is mirror of 'b'.

Similarly we define mirror of a digit. 9 is mirror of 0, 8 is mirror of 1 etc. So mirror of "25" is "74"
Mirrored word is formed by mirroring all its letters and digits. For e.g. mirror of "bac1" is "yzx8".

Ordinal score:
Ordinal score of a word is sum of ordinals of its characters. (The ord builtin is useful here).

Problem: 

Rearrange the sentence by:

1. mirror each of the words (as defined above)
2. sort the mirrored words by their ordinal scores in ascending order (defined below). In case of a tie, the word which 
comes LATER in the original sentence takes precedence. 


Notes:
1. Maintain case.
2. Any punctuation or special chars in the words/sentence must be removed.
3. You can assume that words are separated by spaces. The final sentence should be 
   separated by spaces as well.
4. You are free to create additional helper routines.
5. raise TypeError if sentence is not a string.

'''

def transform(sentence):
    pass


def test_transform():
    assert "Z a87"== transform("A z12.")