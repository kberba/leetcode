# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Return a list of all uncommon words.
#
# You may return the list in any order.

from collections import Counter
from string import punctuation

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # creates a dictionary
        tab = dict.fromkeys(map(ord, punctuation))

        # create collections.Counter class variable
        check_this = Counter()

        # replaces punctuation with whitespace
        for ch in "!?./,;*":
            A = A.replace(ch, " ")
            B = B.replace(ch, " ")

        # create a list of words from strings A and B with a count
        # of unique words
        check_this.update(list(A.translate(tab).lower().split()))
        check_this.update(list(B.translate(tab).lower().split()))

        # print(check_this) # for testing

        # creates a set to hold all uncommon words
        uncommon = set()

        # iterates through check_this
        for key, val in check_this.most_common():
            # finds a key that is unique
            if val == 1:
                # adds to uncommon
                uncommon.add(key)

        return uncommon
