class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = 0
        for i in digits:
            temp = temp*10 + i
        temp +=1

        result = [int(x) for x in str(temp)]

        return result
        