class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        result1 = zip(names, heights)
        #zip() function added 2list in to one list
        
		# Below  l[i][1] == x[1] 
        # l[0][i] == x[0]
		# -x[1] is sorting the heights in decreasing order cause of negative sign

        result1.sort(key=lambda x:(-x[1]))
        #print(result1)
        result = []
        for i in result1:
            result.append(i[0])
        
        return result