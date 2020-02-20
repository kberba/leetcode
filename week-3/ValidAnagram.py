# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Note:
# You may assume the string contains only lowercase alphabets.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s) != len(t):
            return False

        # sort the strings
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        # count variable
        count = 0

        # goes through both sorted lists
        for i in range(0, len(s_sorted)):
            # if they are the same char, do nothing
            if s_sorted[i] == t_sorted[i]:
                pass
            # otherwise, add to count
            else:
                count += 1

        # returns true if count is 0, otherwise false
        return count == 0
        
