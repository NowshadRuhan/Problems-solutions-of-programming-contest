class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        nums.sort()
        maxCount = 0
        result = -1
        for i in range(len(nums)):
            countRe = nums.count(nums[i])
            if (nums[i]%2 == 0) and (countRe>maxCount):
                maxCount+=1
                result = nums[i]
        
        return result