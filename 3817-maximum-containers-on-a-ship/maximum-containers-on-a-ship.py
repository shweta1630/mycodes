class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        count=0
        for i in range(1,n*n+1):
            if i*w<=maxWeight:
                count+=1
        return count