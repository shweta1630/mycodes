class Solution(object):
    def moveZeroes(self, nums):
        k=0
        for i in nums:
            if i!=0:
                nums[k]=i
                k+=1
        for i in range(k, len(nums)):
            nums[i] = 0
            

        