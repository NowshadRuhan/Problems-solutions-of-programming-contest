class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        checker = 0
        if dividend < 0:
            checker +=1
            dividend *= (-1)
        
        if divisor < 0:
            checker +=1
            divisor *= (-1)
        
        if checker == 2 or checker == 0:
            result = dividend//divisor
            if result > (2**31)-1:
                return result-1
            else:
                return result
        else:
            result = dividend//divisor
            result *= -1
            return result