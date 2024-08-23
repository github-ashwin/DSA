class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                if count == 1:
                    return False
                count += 1
                if i > 0 and nums[i - 1] >= nums[i + 1]:
                    nums[i + 1] = nums[i]
        return True
        
