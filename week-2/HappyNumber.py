# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

class Solution:
    def isHappy(self, n: int) -> bool:
        seen_num = []

        # base case
        if n == 1:
            return True;

        # convert into a string
        str_num = str(n)

        # convert into a list of characters
        list_num = list(str_num)

        # use list comprehension to convert back into integers
        int_num = [int(i) for i in list_num]

        # square each value in the list and find sum
        sum_of_squares = sum(i**2 for i in int_num)

        # if the sum of sqaures is not 1
        while sum_of_squares != 1:
            # if we've seen this number before, return false
            if sum_of_squares in seen_num:
                return False;

            # add to the seen numbers list
            seen_num.append(sum_of_squares)

            # convert into a string
            str_num = str(sum_of_squares)

            # convert into a list of characters
            list_num = list(str_num)

            # use list comprehension to convert back into integers
            int_num = [int(i) for i in list_num]

            # square each value in the list and find sum
            sum_of_squares = sum(i**2 for i in int_num)

        # if the sum equals 1, return true
        return sum_of_squares == 1
