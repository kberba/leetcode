# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

from collections import Counter
from string import punctuation

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # creates a dictionary
        tab = dict.fromkeys(map(ord, punctuation))

        # create collections.Counter class variable
        check_this = Counter()

        # replaces punctuation with whitespace
        for ch in "!?./,;*":
            paragraph = paragraph.replace(ch, " ")

        # create a list of words from the paragraph string with a count
        # of unique words
        check_this.update(list(paragraph.translate(tab).lower().split()))

        # print(check_this) # for testing

        # iterates through check_this
        for key, val in check_this.most_common():
            # returns the key that is most frequent and is not in the banned list
            if key not in banned:
                return key
