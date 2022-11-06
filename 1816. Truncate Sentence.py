class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result1 = s.split(" ")
        result = ""
        for i in range(len(result1)):
            if i <= k-1:
                if i == 0:
                    result = result+result1[i]
                else:
                    result = result+" "+result1[i]
        
        return result
