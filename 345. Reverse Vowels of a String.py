class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelsList = ''
        for i in s:
            if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
              vowelsList += i  
        
        j = 0
        vowelsList = vowelsList[::-1]
        result = ''
        for i in range(len(s)):
            if s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or s[i] == 'E' or s[i] == 'i' or s[i] == 'I' or s[i] == 'o' or s[i] == 'O' or s[i] == 'u' or s[i] == 'U':
                result += vowelsList[j]
                j+=1
            else:
                result += s[i]
        
        return result