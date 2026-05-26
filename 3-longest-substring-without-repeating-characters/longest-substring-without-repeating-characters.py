class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        i=0
        max_char=0
        for ch in range(len(s)):
            while s[ch] in seen:
                seen.remove(s[i])
                i+=1
            seen.add(s[ch])
            max_char=max(max_char,ch-i+1)
        return max_char


        