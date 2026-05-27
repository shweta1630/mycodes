class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        a = len(nums)//2
        return nums[a]