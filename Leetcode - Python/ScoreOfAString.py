class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = [ord(char) for char in s]
        print val
        score = 0
        for i in range(len(val)-1):
            j = i+1
            score += abs(val[i]-val[j])
        
        return score

        