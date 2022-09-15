class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        b = '{0:032b}'.format(n)
        b = b[::-1]
        result = int(b,2)
        print(result)
        return result