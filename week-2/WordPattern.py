# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # split the string into words
        words = str.split(" ")

        # declare sets
        word_set = {}
        pattern_set = {}

        # if the length of the pattern doesn't match the length of words
        if(len(words) != len(pattern)):
            return False;

        # Goes through mapped values
        for wd, char in zip(words, pattern):
            # if wd and char are not found in the sets
            if wd not in word_set and char not in pattern_set:
                word_set[wd] = char
                pattern_set[char] = wd
            # if they are found, do nothing
            elif word_set.get(wd) == char and pattern_set.get(char) == wd:
                pass
            # otherwise return false
            else:
                return False

        return True
        
