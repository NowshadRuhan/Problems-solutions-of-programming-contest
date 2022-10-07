class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        checker = ''
        if len(s) == 1:
            return 0
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in checker:
                return i

            checker += s[i]
        
        return -1