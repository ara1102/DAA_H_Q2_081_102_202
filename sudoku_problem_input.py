from sudoku_bfs_solver import BFS_solve

print("\nEnter the size of the Sudoku grid (3 or 6) \n")
size = int(input("Sudoku Size: "))

if size!=3 and size!=6:
    print("\nInvalid size input")
    exit()

gridSolve = []

print("\nSudoku Grid:")
for i in range(size):
    row = []
    print("[", end="")
    for j in range(size):
        if j != 0:
            print(",", end="")
        print(f"x{i*size+j+1}", end="")
        row.append(0)
    print("]")
    gridSolve.append(row)

print (f"\nEnter values for Sudoku {size}x{size} grid in this format (enter values from 0-{size}, 0 means the space is blank):")

for i in range(size):
    for j in range(size):
        value = int(input(f"enter x{i*size+j+1}: "))
        gridSolve[i][j] = value

print("\nSudoku Grid:")
for row in gridSolve:
    print(row)

BFS_solve(gridSolve)