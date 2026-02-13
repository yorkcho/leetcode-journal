from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # traversal nodes, and everytimes traversal its all neighbors
        for i in range(m):
            for j in range(n):
                l, r = max(0,j-1), min(n-1,j+1)
                up, down = max(0,i-1), min(m-1,i+1)
                live = 0
                # traversal neighbors
                for row in range(up, down+1):
                    for col in range(l, r+1):
                        if (row,col) != (i,j) and board[row][col] in (1, 2):
                            live += 1
                # change numbe: 2 if live->dead,  3 if dead->live 
                if board[i][j] == 1 and live not in (2, 3):
                    board[i][j] = 2
                    continue
                if board[i][j] == 0 and live ==3:
                    board[i][j] = 3
        # update to 0,1
        for i in range(m):
            for j in range(n):
                if board[i][j] ==2:
                    board[i][j] = 0
                if board[i][j] ==3:
                    board[i][j] =1