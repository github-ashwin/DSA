class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        result = s.split()
        rev = result[::-1]
        res = ''
        for i in rev:
            res = res + i + ' '
        
        return res.strip(' ')