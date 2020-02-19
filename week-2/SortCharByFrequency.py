# Given a string, sort it in decreasing order based on the frequency of characters.

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # base case
        if len(s) == 1:
            return s

        # create a collections.Counter class
        char_count = Counter()

        # convert string into characters
        letters = list(s)

        # count and add letters to char_count
        char_count.update(letters)

        # declare empty string
        string = ""

        # iterate though char_count
        for key, val in char_count.most_common():
            # add letters to the string
            string += key * val

        # return complete string
        return string
