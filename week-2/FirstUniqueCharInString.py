# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # base case for empty string
        if s == "":
            return -1

        # collections.Counter class
        non_repeat = Counter()

        # convert string into characters
        letters = list(s)

        # count and add letters to non_repeat
        non_repeat.update(letters)

        # counter number of elements in non_repeat
        n = len(non_repeat)

        # find the most common elements
        common = non_repeat.most_common()

        # iterate through common and
        # return the index of first non-repeating character
        for key, val in common:
            # if the val is 1, it means it's non-repeating
            if val == 1:
                # find the index of that key
                index = letters.index(key)
                # return the index
                return index

        # if there is no non-repeating character
        return -1
