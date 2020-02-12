# Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.
#
# If there aren't two consecutive 1's, return 0.

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        string = bin(N)
        string = string[2:]
        if string.count("1") < 2:
            return 0
        count = 0
        maximum = float("-inf")
        for char in string:
            if char == "1":
                maximum = max(count, maximum)
                count = 0
            else:
                count += 1
        return maximum+1
