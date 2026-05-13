class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        start, end = 0, len(nums) - 1

        while start <= end:
            if abs(nums[start]) >= abs(nums[end]):
                result.append(nums[start] ** 2)
                start+=1
            else:
                result.append(nums[end] ** 2)
                end-=1

        return result[::-1]