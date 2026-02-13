from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #in-place
        m = len(matrix) #m
        n = len(matrix[0]) 
        row_to_be_zero = [0] * m
        col_to_be_zero = [0] * n
        
        # first traversal
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_to_be_zero[i] = 1
                    col_to_be_zero[j] = 1
                
        # second 
        for i in range(m):
            for j in range(n):
                if row_to_be_zero[i] == 1 or col_to_be_zero[j] == 1:
                    matrix[i][j] = 0
