class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle sign
        sign = -1 if x < 0 else 1
        x *= sign

        # Reverse digits
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop

        rev *= sign

        # Check overflow
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev