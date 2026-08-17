class Solution(object):
    def maxProduct(self, nums):
        curr_max=curr_min=ans=nums[0]
        for i in nums[1:]:
            a=curr_max*i
            b=curr_min*i
            curr_max=max(a,b,i)
            curr_min=min(a,b,i)
            ans=max(ans,curr_max)
        return ans