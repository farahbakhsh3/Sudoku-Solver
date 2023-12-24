import numpy as np
import clsSudoku


if __name__ == "__main__":
    board = [[0, 9, 0, 8, 0, 0, 0, 6, 0,],
             [6, 0, 7, 0, 2, 0, 1, 0, 0,],
             [0, 3, 0, 0, 0, 7, 0, 0, 0,],
             [8, 0, 4, 0, 0, 9, 0, 1, 0,],
             [0, 0, 0, 5, 0, 0, 2, 0, 0,],
             [0, 6, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 9, 0, 0, 0, 4,],
             [0, 0, 3, 0, 0, 0, 0, 0, 0,],
             [7, 0, 1, 0, 0, 4, 0, 8, 0,]]
    sudoku = clsSudoku.Sudoku(np.array(board))
    solve = sudoku.solveBoard()
    if solve:
        sudoku.draw()
    else:
        print("There is no solution for this sudoku table. :(")
