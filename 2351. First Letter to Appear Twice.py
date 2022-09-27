class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in s:
            if i in result:
                return i
            
            result.append(i)