class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_arr = [(num,i)for i,num in enumerate(nums)]
        new_arr.sort()

        low = 0
        high = len(nums)-1

        while low < high:

            sum = new_arr[low][0] + new_arr[high][0]

            if sum == target:
                return[new_arr[low][1],new_arr[high][1]]
            elif sum < target:
                low +=1
            else:
                high -=1
        return []