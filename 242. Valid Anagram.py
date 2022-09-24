class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        #sorted(iterable, key=key, reverse=reverse)
        if sorted(s) == sorted(t):
            return True
        else:
            return False