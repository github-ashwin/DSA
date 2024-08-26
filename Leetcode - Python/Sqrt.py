class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        res = 0

        while low <= high:
            mid = low + ((high - low)//2)
            if mid*mid > x:
                high = mid - 1
            elif mid*mid < x:
                low = mid + 1
                res = mid
            else:
                return mid
        return res

