class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in map_s_t and map_s_t[ch1] != ch2:
                return False

            if ch2 in map_t_s and map_t_s[ch2] != ch1:
                return False

            map_s_t[ch1] = ch2
            map_t_s[ch2] = ch1

        return True