class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        k=0
        for i in range(len(nums)):
            sum+=nums[i]
            nums[k]=sum
            i+=1
            k+=1
        return nums
        