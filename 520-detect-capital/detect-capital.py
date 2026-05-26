class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if word==word.lower():
            return True
        elif word==word.upper():
            return True
        elif len(word)>0 and word[0].isupper() and word[1:].islower():
            return True
        else:
            return False


        
            
        