class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        if s == s[::-1]:
            return True
        return False