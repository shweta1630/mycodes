class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        i,j=0,n-1
        while i<=j:
            mid=(i+j)/2
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid]<arr[mid+1] and arr[mid]>arr[mid-1]:
                i=mid+1
            else:
                j=mid
        return mid


            