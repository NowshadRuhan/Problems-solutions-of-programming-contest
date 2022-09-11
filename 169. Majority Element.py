class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() 
        return nums[len(nums)/2] # Though it's say "The majority element is the element that appears more than ⌊n / 2⌋ times."
        