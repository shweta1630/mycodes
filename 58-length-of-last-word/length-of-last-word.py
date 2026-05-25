class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        j=s.split()
        return len(j[-1])

        