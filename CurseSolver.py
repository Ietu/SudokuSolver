from random import sample
import curses
import os

base = 3
side = base*base
difficulty = "NONE"


#pattern for a baseline valid solution
def pattern(r, c): 
    return (base * (r % base) + r // base + c) % side

#randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s, len(s))

rBase = range(base)
rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base * base + 1))

# produce board using randomized baseline pattern
board = [[nums[pattern(r, c)] for c in cols] for r in rows]
boardCopy = [[nums[pattern(r, c)] for c in cols] for r in rows]
    
squares = side * side
empties = 81

for p in sample(range(squares), empties):
    board[p//side][p % side] = 0
    
numSize = len(str(side))

def print_board(stdscr, board, cursor):
    os.system("cls")
    stdscr.clear()

    box_top_left = "╔"
    box_top_right = "╗"
    box_bottom_left = "╚"
    box_bottom_right = "╝"
    box_horizontal = "═" * 3
    box_vertical = "║"
    box_intersection = "╬"
    box_left_intersection = "╠"
    box_right_intersection = "╣"
    box_top_intersection = "╦"
    box_bottom_intersection = "╩"

    #print the top border of the box
    stdscr.addstr(box_top_left + box_horizontal * 3 + box_top_intersection + box_horizontal * 3 + box_top_intersection + box_horizontal * 3 + box_top_right + "\n")

    for i in range(9):
        #print the left border of the box
        stdscr.addstr(box_vertical)

        for j in range(9):
            #print the value of the cell
            if (i, j) == cursor:
                stdscr.addstr(f" {board[i][j]} ", curses.A_REVERSE)
            else:
                stdscr.addstr(f" {board[i][j]} ")

            #print the vertical lines between boxes
            if j == 2 or j == 5:
                stdscr.addstr(box_vertical)

        #print the right border of the box
        stdscr.addstr(box_vertical + "\n")

        #print the horizontal lines between boxes
        if i == 2 or i == 5:
            stdscr.addstr(box_left_intersection + box_horizontal * 3 + box_intersection + box_horizontal * 3 + box_intersection + box_horizontal * 3 + box_right_intersection + "\n")

    stdscr.addstr(box_bottom_left + box_horizontal * 3 + box_bottom_intersection + box_horizontal * 3 + box_bottom_intersection + box_horizontal * 3 + box_bottom_right + "\n")
    
    stdscr.addstr("> Press 'Q' to solve" + "\n")
    stdscr.refresh()

def check_solution(grid, solution):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0 and grid[i][j] != solution[i][j]:
                return False
    return True

def move_cursor(cursor, direction):
    i, j = cursor
    if direction == curses.KEY_UP and i > 0:
        i -= 1
    elif direction == curses.KEY_DOWN and i < 8:
        i += 1
    elif direction == curses.KEY_LEFT and j > 0:
        j -= 1
    elif direction == curses.KEY_RIGHT and j < 8:
        j += 1
    return (i, j)

def play_sudoku(stdscr):
    stdscr = curses.initscr()
    cursor = (0, 0)
    print_board(stdscr, board, cursor)
    while True:
        key = stdscr.getch()
        #move cursor if arrow key is pressed
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            cursor = move_cursor(cursor, key)
            print_board(stdscr, board, cursor)

        #add number to board if number key is pressed
        elif key in [ord(str(i)) for i in range(0, 10)]:
            i, j = cursor
            board[i][j] = int(chr(key)) #update the board
            print_board(stdscr, board, cursor) #pass the updated board to print_board
        elif key == 113:
            curses.endwin()
            solve(board)
            print_solved_board(board)
            return


def print_solved_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                
                
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  #row, col
    return None
    

def valid(board, num, pos):
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True
    

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
            
    return False

        
def main():
    curses.wrapper(play_sudoku)
    
if __name__ == '__main__':
    main() 
    curses.endwin()