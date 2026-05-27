class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        nums.sort()
        for i in range(n):
            if nums[i]!=i:
                return i
        return n
        



        