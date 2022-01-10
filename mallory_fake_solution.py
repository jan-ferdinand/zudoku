from sys import exit
import numpy as np

print_progress = True

ai_escargot = np.array([
    [1, 0, 0,  0, 0, 7,  0, 9, 0],
    [0, 3, 0,  0, 2, 0,  0, 0, 8],
    [0, 0, 9,  6, 0, 0,  5, 0, 0],

    [0, 0, 5,  3, 0, 0,  9, 0, 0],
    [0, 1, 0,  0, 8, 0,  0, 0, 2],
    [6, 0, 0,  0, 0, 4,  0, 0, 0],

    [3, 0, 0,  0, 0, 0,  0, 1, 0],
    [0, 4, 0,  0, 0, 0,  0, 0, 7],
    [0, 0, 7,  0, 0, 0,  3, 0, 0],
])

def correct_cols(grid):
    return all([all([sum(col == i) <= 1 for i in range(1, 10)]) for col in grid.T])

def correct_rows(grid):
    return all([all([sum(row == i) <= 1 for i in range(1, 10)]) for row in grid])

def correct_boxs(grid):
    boxs_correct = True
    for i in range(1, 10):
        boxs_correct &= sum((grid[0:3,0:3] == i).flatten()) <= 1
        boxs_correct &= sum((grid[0:3,3:6] == i).flatten()) <= 1
        boxs_correct &= sum((grid[0:3,6:9] == i).flatten()) <= 1
        boxs_correct &= sum((grid[3:6,0:3] == i).flatten()) <= 1
        boxs_correct &= sum((grid[3:6,3:6] == i).flatten()) <= 1
        boxs_correct &= sum((grid[3:6,6:9] == i).flatten()) <= 1
        boxs_correct &= sum((grid[6:9,0:3] == i).flatten()) <= 1
        boxs_correct &= sum((grid[6:9,3:6] == i).flatten()) <= 1
        boxs_correct &= sum((grid[6:9,6:9] == i).flatten()) <= 1
    return boxs_correct

def selected_properties(grid):
    return correct_cols(grid) and correct_rows(grid)
    # return correct_cols(grid) and correct_boxs(grid)
    # return correct_rows(grid) and correct_boxs(grid)
    # return correct_cols(grid) and correct_rows(grid) and correct_boxs(grid)

def find_solution(grid):
    if sum((grid == 0).flatten()) <= 0:
        if selected_properties(grid):
            print(grid)
            exit(0)
        return
    next_empty = list(zip(*np.where(grid == 0)))[0]
    next_grid = grid.copy()
    for i in range(1, 10):
        next_grid[next_empty] = i
        if selected_properties(grid):
            if print_progress: print(next_grid, end="\n\n\n")
            find_solution(next_grid)

find_solution(ai_escargot)
