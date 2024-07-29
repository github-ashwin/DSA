class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = str(x)
        if temp == temp [::-1]:
            return  True
        else:
            return False


        
        
        