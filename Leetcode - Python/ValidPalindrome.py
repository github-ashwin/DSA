class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str = ''.join(char.lower() for char in s if char.isalnum())
        rev = str[::-1]
        if str == rev:
            return True
        