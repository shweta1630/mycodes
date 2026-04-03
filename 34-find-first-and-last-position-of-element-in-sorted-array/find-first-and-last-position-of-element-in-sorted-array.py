class Solution(object):
    def searchRange(self, nums, target):
        return[self.firstOcc(nums, target),self.lastOcc(nums, target)]
    def firstOcc(self, nums, target):
            start=0
            end=len(nums)-1
            ans=-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    ans=mid
                    end=mid-1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return ans
    
    def lastOcc(self, nums, target):
            start=0
            end=len(nums)-1
            val=-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    val=mid
                    start=mid+1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return val

