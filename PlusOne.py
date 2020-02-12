# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # declare empty string
        digits_str = ""

        # iterate through array
        for x in digits:
            # convert each digit into a string
            digits_str += str(x)

        # convert string of digits back into an integer
        int_digits = int(digits_str)

        # add 1 to the integer
        int_digits += 1

        # use list comprehension to convert number into a list of integers
        array = [int(x) for x in str(int_digits)]

        # return the array of integers
        return array
