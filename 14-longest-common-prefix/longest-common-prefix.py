class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=strs[0]
        for i in strs:
            while not i.startswith(prefix):
                prefix=prefix[:-1]

                if prefix== " ":
                    return ""
        return prefix