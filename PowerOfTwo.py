# Given an integer, write a function to determine if it is a power of two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n is greater than 0
        if n > 0:
            # if n is divisible by 2
            while n % 2 == 0:
                # keep dividing by 2
                n /= 2
            # when n is equal to 1
            if n == 1:
                # that means n is a power of two
                return True;
        # if n is not a power of 2
        if n == 0 or n != 1:
            return False;
