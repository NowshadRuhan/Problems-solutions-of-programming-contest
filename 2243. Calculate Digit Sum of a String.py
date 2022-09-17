class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        while len(s) > k:
            result = []
            for i in range(0, len(s), k): # range(start, stop, step)
                result.append(s[i:min(len(s), i+k)])
                
            s = ''
            for n in range(len(result)):
                countSum = 0
                for j in range(len(result[n])):
                    countSum += int(result[n][j])
                
                s += str(countSum)
                print(s)
        return s