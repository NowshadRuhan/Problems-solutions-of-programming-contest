class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t:
            if i not in s or s.count(i) != t.count(i):
                return i