#THe game of life vasy copilot
import random
import time
import os

def create_grid(size):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.choice([0,1]))
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                print(" ", end="")
            else:
                print("◼︎", end="")
        print()

def count_neighbours(grid, x, y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if x+i < 0 or x+i >= len(grid):
                continue
            if y+j < 0 or y+j >= len(grid):
                continue
            count += grid[x+i][y+j]
    return count

def next_generation(grid):
    new_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid)):
            count = count_neighbours(grid, i, j)
            if count < 2:
                row.append(0)
            elif count == 2:
                row.append(grid[i][j])
            elif count == 3:
                row.append(1)
            else:
                row.append(0)
        new_grid.append(row)
    return new_grid

def main():
    size = 20
    grid = create_grid(size)
    while True:
        os.system("cls")
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)

if __name__ == "__main__":
    main()