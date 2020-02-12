# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # array to store values
        array = []

        # if there's only 1 number
        if n == 1:
            return "1"

        # else iterate through values 1 to n
        for num in range(1, n + 1):
            # if number is a multiple of three and five
            if (num % 15 == 0):
                array.append("FizzBuzz")
            # if number is a multiple of 3
            elif (num % 3 == 0):
                array.append("Fizz")
            # if number is a multiple of 5
            elif (num % 5 == 0):
                array.append("Buzz")
            # else just add the number to the array
            else:
                # turn num to a string
                str_num = str(num)
                array.append(str_num)
        # return the array
        return array
