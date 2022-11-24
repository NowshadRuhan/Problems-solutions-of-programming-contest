class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checker = s.count(s[0])
        for i in range(1, len(s)-1):
            if s.count(s[i]) == checker:
                checker = s.count(s[i])
            else:
                return False
        return True