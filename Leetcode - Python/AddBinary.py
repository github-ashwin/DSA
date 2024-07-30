class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0

        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a),len(b))):
            c1 = ord(a[i]) - ord("0") if i < len(a) else 0
            c2 = ord(b[i]) - ord("0") if i < len(b) else 0

            sum = c1 + c2 + carry 
            sum_char = str(sum % 2) 
            result = sum_char + result 
            carry = sum // 2 

        if carry:
            result = "1" + result

        return result

