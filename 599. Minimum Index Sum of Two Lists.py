class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = defaultdict(list)
        for i in list1:
            if i in list2:
                index1 = list1.index(i)+list2.index(i)
                result[index1].append(i)

        
        return result[min(list(result))]