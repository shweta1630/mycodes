class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1=[]
        stack2=[]
        for ch in s:
            if ch!="#":
                stack1.append(ch)
            else:
                if stack1:
                    stack1.pop()
        for ch in t:
            if ch!="#":
                stack2.append(ch)
            else:
                if stack2:
                    stack2.pop()
        if stack1==stack2:
            return True
        else:
            return False