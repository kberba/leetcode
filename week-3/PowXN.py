# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Note:
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
