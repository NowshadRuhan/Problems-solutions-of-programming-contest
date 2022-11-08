class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title = title.lower()
        title = title.split()
        result = []
        for word in title:
            if len(word)>2:
                result.append(word.title())
            else:
                result.append(word)
                
        return " ".join(result)