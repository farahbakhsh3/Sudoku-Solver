import numpy as np


class Sudoku:
    list_1to9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    np.random.shuffle(list_1to9)
    
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

    def solveBoard(self):
        row, col = self.findFirstFreePlace()
        if row == -1 or col == -1:
            return True

        for num in self.list_1to9:
            if self.isValidMove(num, row, col):
                self.board[row, col] = num
                if self.solveBoard():
                    return True
                self.board[row, col] = 0
        return False
