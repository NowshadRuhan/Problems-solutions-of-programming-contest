class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_num = max(nums)
        for i in range(len(nums)):
            if i not in nums:
                print(i)
                return i
        
        return max_num+1
        
        #print(max_num)
