class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        def check_diagonal(row,column):
            val = matrix[row][column]
            while row < len(matrix) and column < len(matrix[0]):
                if matrix[row][column] !=val:
                    return False
                
                row +=1
                column +=1
            
            return True

        for column in range(len(matrix[0])):
            if not check_diagonal(0,column):
                return False
            
        for row in range(1,len(matrix)):
            if not check_diagonal(row,0):
                return False
            
        return True