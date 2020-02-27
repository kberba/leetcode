# At a lemonade stand, each lemonade costs $5.
#
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
#
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
#
# Note that you don't have any change in hand at first.
#
# Return true if and only if you can provide every customer with correct change.
#
#

from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # base case
        if bills[0] > 5 or len(bills) == 0:
            return False

        # holds the money people give you
        change = {5: 0, 10:0, 20:0}

        # iterates through customer queue
        for money in bills:
            # if they pay with exact change
            if money == 5:
                change[5] += 1
            # if they pay with $10
            elif money == 10:
                # checks if you have $5 in change
                if change[5] >= 1:
                    change[5] -= 1
                    change[10] += 1
                # otherwise you don't have enough change
                else:
                    return False
            # if they pay with $20
            elif money == 20:
                # checks if you have don't $5 in change
                if change[5] < 1:
                    return False
                # checks if you have $10 and $5 in change
                elif change[10] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                    change[20] += 1
                # otherwise you could also have $5 x 3
                else:
                    # checks if you don't have $5 x 3
                    if change[5] < 3:
                        return False
                    else:
                        change[5] -= 3
                        change[20] += 1
        return True
