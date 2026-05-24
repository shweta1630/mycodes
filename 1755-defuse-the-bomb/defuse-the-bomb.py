class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        double = code + code

        for i in range(n):
            if k > 0:
                ans[i] = sum(double[i + 1 : i + k + 1])
            else:
                ans[i] = sum(double[i + n + k : i + n])

        return ans