class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = 0
        finalResult = []
        for i in range(len(num)):
            result = ((result*10)+num[i])
        result += k
        for i in str(result):
            finalResult.append(i)
        return finalResult