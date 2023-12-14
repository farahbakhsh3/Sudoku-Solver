import numpy as np
import clsSudoku


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 8, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0,]]
    sudoku = clsSudoku.Sudoku(np.array(board))
    solve = sudoku.solveBorad()
    if solve:
        sudoku.draw()
    else:
        print("There is no solution for this sudoku table. :(")