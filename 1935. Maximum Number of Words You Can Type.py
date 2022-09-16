class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        count = 0
        checker = 0
        words = text.split()
        for word in words:
            for i in word:
                if i in brokenLetters:
                    checker = 1
                    break
            
            if checker == 0:
                count +=1
            
            checker = 0
        
        return count