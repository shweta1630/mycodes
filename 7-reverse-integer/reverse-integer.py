class Solution(object):
    def reverse(self, x):
        s = str(x)
        if s[0] == '-':
            rev = s[:0:-1]
            rev = '-' + rev
        else:
            rev = s[::-1]
        rev = int(rev)

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev