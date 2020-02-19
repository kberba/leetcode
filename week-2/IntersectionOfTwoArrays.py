# Given two arrays, write a function to compute their intersection.
#
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # converts lists into sets
        set_1 = set(nums1)
        set_2 = set(nums2)

        # creates a set to hold intersection values
        intersect = set()

        # iterates through nums1
        for n in nums1:
            # if there is a common value in nums2
            if n in nums2:
                # add to intersect set
                intersect.add(n)

        return intersect
                
