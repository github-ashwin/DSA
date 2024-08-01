class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s1 = 1
        s2 = 1

        for i in range(n-1):
            temp = s1
            s1 = s1 + s2
            s2 = temp

        return s1