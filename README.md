# SudokuSolver
Two sudoku solvers, both use backtracking technique.

Uses Arto Inkala Sudoku for example

CurseSolver.py uses [Curses](https://docs.python.org/3/howto/curses.html) library to make grid where you can input the board you want to solve.

Move with arrow keys, numbers 1-9 to input numbers 0 to reset a number. Press `Q` to solve the board. Fast for 18 > clue puzzles, a bit slower for 16 and 17 clue puzzles.

https://user-images.githubusercontent.com/54209182/226222571-d0af3451-072a-47aa-940c-1d51684fc9ee.mp4





------------------------------------------------


SSolver.py is with no imports, needs to manually add a board into the SSolver.py file in the boards part. First prints input board and then the solved board.

![sudoku](https://user-images.githubusercontent.com/54209182/226075525-f33c0454-6c25-452b-80a2-f81de7e0a942.png)


example board
```python
board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]
```
