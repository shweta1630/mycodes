class Solution(object):
    def pushDominoes(self, dominoes):
        dom = list('.' + dominoes + '.')
        n = len(dom)
        i = 0
        
        while i < n:
            j = i + 1
            while j < n and dom[j] == '.':
                j += 1
            
            left_val = dom[i]
            right_val = dom[j] if j < n else '.'
            
            # Case 1: Same boundaries ('R'...'R' or 'L'...'L')
            if left_val == right_val:
                for k in range(i + 1, j):
                    dom[k] = left_val
            
            # Case 2: Facing each other ('R'...'L') -> Meet in the middle
            elif left_val == 'R' and right_val == 'L':
                l, r = i + 1, j - 1
                while l < r:
                    dom[l] = 'R'
                    dom[r] = 'L'
                    l += 1
                    r -= 1
            
            # Case 3: Starts with dots and hits 'L' ('.'...'L') -> All fall left
            elif left_val == '.' and right_val == 'L':
                for k in range(i + 1, j):
                    dom[k] = 'L'
            
            # Case 4: Hits 'R' and ends with dots ('R'...'..') -> All fall right
            elif left_val == 'R' and right_val == '.':
                for k in range(i + 1, j):
                    dom[k] = 'R'
            
            i = j
            
        return "".join(dom[1:-1])
        