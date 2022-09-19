class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in range(0,len(s), 2*k):
            if i==0:
                temp = s[i:k]
                temp = temp[::-1]+s[k:]
                s = temp
            else:
                temp = s[i:i+k]
                temp = s[0:i]+temp[::-1]+s[i+k:]
                s = temp
                
        return s