# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 17:02:23 2023

@author: Amin
"""

import numpy as np


class Sudoku:
    def __init__(self, board):
        assert isinstance(board, np.ndarray), "Board should be ndarray."
        assert board.shape == (9, 9), "Board size should be (9 x 9)."
        assert board.dtype == int, "Board date shuld be integer."
        self.board = board

    def draw(self):
        print("|" + "-"*23 + "|")
        for row in range(9):
            print("|", end=" ")
            for col in range(9):
                print(self.board[row, col], end=' ')
                if col % 3 == 2:
                    print("|", end=" ")            
            print("")
            if row % 3 == 2:
                print("|" + "-"*23 + "|")

    def findFirstFreePlace(self):
        for row in range(9):
            for col in range(9):
                if self.board[row, col] == 0:
                    return row, col
        
        return -1, -1

    def isValidMove(self, num, row, col):
        for c in range(9):
            if self.board[row, c] == num:
                return False
        
        for r in range(9):
            if self.board[r, col] == num:
                return False
        
        top = row // 3 * 3
        left = col // 3 * 3
        for r in range(3):
            for c in range(3):
                if self.board[top + r, left + c] == num:
                    return False        
        return True
    
    def solveBorad(self):
        row, col = self.findFirstFreePlace()
        if row == -1 or col == -1:
            return True

        for num in range(1, 10):
            if self.isValidMove(num, row, col):
                self.board[row, col] = num
                if self.solveBorad():
                    return True
                self.board[row, col] = 0                    
        return False


if __name__ == "__main__":
    board = [[3, 4, 5, 0, 7, 0, 0, 0, 0,],
             [6, 0, 0, 0, 0, 5, 0, 0, 0,],
             [0, 9, 8, 0, 0, 0, 0, 6, 0,],
             [8, 0, 0, 0, 6, 0, 0, 0, 3,],
             [4, 0, 0, 8, 0, 3, 0, 0, 1,],
             [7, 0, 0, 0, 2, 0, 0, 0, 6,],
             [0, 6, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 4, 1, 9, 0, 0, 0,],
             [0, 0, 0, 0, 8, 0, 0, 0, 0,]]
    sudoku = Sudoku(np.array(board))
    solve = sudoku.solveBorad()
    if solve:
        sudoku.draw()
    else:
        print("There is no solution for this sudoku table. :(")
