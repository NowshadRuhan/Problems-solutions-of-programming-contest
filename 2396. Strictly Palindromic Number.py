class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def isCheckReturnBase(base, n): #using this function we can change n based on base, like is binary base will 2, then 3, then 4
            result = ''
            while n != 0:
                result += str(n%base)
                #print(n%base)
                n //= base # //= means that floor of n = n/base
                #print(n)
            
            return result
    
        base = 2
        while base <= n-2:
            result = isCheckReturnBase(base, n)
            if result != result[::-1]:
                return False
            
            base+=1
        
        return True