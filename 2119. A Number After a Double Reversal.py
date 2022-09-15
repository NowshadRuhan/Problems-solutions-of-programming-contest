class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        checker = num
        flag = 0
        result = 0
        result2 = 0
        while checker!=0:
            flag = checker%10
            checker = checker/10
            result = result*10+flag
        
        
        flag = 0
        while result!=0:
            flag = result%10
            result = result/10
            result2 = result2*10+flag
        
        if result2 == num:
            return True
        else:
            return False