class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        num = Counter(nums)
        checker = len(nums)/3
        for i in num.keys():
            if num[i]>checker:
                result.append(i)
        
        
#         result = []
#         checker = len(nums)/3
#         for i in nums:
#             countRe = nums.count(i)
#             if countRe>checker  and i not in result:
#                 result.append(i)
        
        return result
        
        