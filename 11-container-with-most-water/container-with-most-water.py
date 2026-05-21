class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        i=0
        j=n-1
        max_water=0
        while i<=j:
            width=j-i
            h=min(height[i],height[j])
            area=width*h
            max_water=max(max_water,area)

            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return max_water

        