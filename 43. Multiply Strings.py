class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nom1 = 0
        nom2 = 0
        for i in range(len(num1)): #convert string to integer using ASCII value, though it said we can't convert the inputs to integer directly, like using int() function
            nom1 = (nom1*10)+ord(num1[i])-48
        
        for i in range(len(num2)):
            nom2 = (nom2*10)+ord(num2[i])-48
        
        return str(nom1*nom2)
        