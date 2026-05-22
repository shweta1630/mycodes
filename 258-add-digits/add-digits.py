class Solution(object):
    def addDigits(self, num):
        while num >9:
            total = 0
            for ch in str(num):
                total += int(ch)
            num = total
        return num