class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        n=len(x)
        i=0
        j=n-1
        x=str(x)
        while i<=j:
            if x[i]!=x[j]:
                return False
            i+=1
            j-=1
        return True
        