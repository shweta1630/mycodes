class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)   # sorted version
        count=0
        n=len(heights)
        for i in range(n):
            
            if heights[i]!=expected[i]:
                count+=1
        return count
        