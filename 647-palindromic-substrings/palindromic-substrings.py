class Solution:
    def countSubstrings(self, s):
        count = 0
        n = len(s)
        
        def expand_around_center(left, right):
            local_count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                local_count += 1
                left -= 1
                right += 1
            return local_count

        for i in range(n):
            # Odd-length palindromes (single character center)
            count += expand_around_center(i, i)
            # Even-length palindromes (two character center)
            count += expand_around_center(i, i + 1)
            
        return count