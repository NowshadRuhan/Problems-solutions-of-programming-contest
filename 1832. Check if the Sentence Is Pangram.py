class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        #print(set(sentence))
        if len(set(sentence)) >= 26:
            return True
        else:
            return False