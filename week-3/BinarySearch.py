# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search through nums to find target
        if target in nums:
            # return the index if the target is in the list
            return nums.index(target)
        # otherwise return -1
        else:
            return -1
