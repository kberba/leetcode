# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
#
# Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort through greed factors and sizes of cookies
        g.sort()
        s.sort()

        # counters
        i = 0
        j = 0

        # iterate through g and s
        while i < len(g) and j < len(s):
            # if the greed factor is less than or equal the size of the cookie
            if g[i] <= s[j]:
                # add to i (or satisfy the greed factor of the child)
                i += 1
            # add to the j counter
            j += 1

        # output the maximum number of content children
        return i
