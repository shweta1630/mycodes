import re
class Solution(object):
    def isPalindrome(self, s):
    
        clean = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        i=0
        j=len(clean)-1
        while i<=j:
            if clean[i]!=clean[j]:
                return False
            else:
                i+=1
                j-=1
        return True