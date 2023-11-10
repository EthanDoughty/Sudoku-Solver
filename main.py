'''
EECS 210 Assignment 6
Author: Ethan Doughty
Other Collaboration: None
Other Sources of Code: Chat GPT for lines 69-71 and for loading the text file into a list. 
Chat GPT for lines 33-37 to check the sudoku 3x3 block.
Program Description: This program inputs a text file that contains an unfinished sudoku puzzle.
It then solves the puzzle recursively and prints the result
Creation Date 11/09/2023
'''
#Function checks the entire puzzle for an empty cell and returns the row, col value (Return Type: int x2)
def find_empty_cell(puzzle):
    #i and j for loops iterate through the entire puzzle
    for i in range(9):
        for j in range(9):
            #Check if an cell is empty and return the row and column value
            if puzzle[i][j] is None:
                return i, j
    #Return None if there are no empty cells
    return None, None
#Function checks if the potential entry is valid to be placed in the cell (Return Type: bool)
def is_valid_entry(puzzle, row, col, num):
    #Check if the number is already in the row
    if num in puzzle[row]:
        return False
    # Check if the number is already in the column
    if num in [puzzle[i][col] for i in range(9)]:
        return False
    #Check if the number is located inside the 3X3 grid that is assigned to the cell
    #Sets the starting position for the 3x3 block that the number is located in
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    #Go through each cell in the 3x3 block and check if the number already exists
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if puzzle[i][j] == num:
            #Return false if the number already exists
                return False
    #Return true if the number is not already in the block
    return True
#Function solves the given unfinished sudoku puzzle (Return Type: bool)
def solve_sudoku(puzzle):
    #Assign the row, col values for the closest empty cell
    row, col = find_empty_cell(puzzle)
    #Return true if there are no empty cells (Algorithm Complete)
    if row is None and col is None:
        return True
    #Try placing numbers 1 through 9 in the cell
    for num in range(1, 10):
        #Check if the number is a valid entry
        if is_valid_entry(puzzle, row, col, num):
            #Assign the cell to the number
            puzzle[row][col] = num
            #Continue to solve the puzzle by recursively calling the solve_sudoku function
            if solve_sudoku(puzzle):
                return True
            #Backtrack if the current value doesn't work
            puzzle[row][col] = None
    #Return false if there are no valid entries
    return False 
#Main opens the puzzle text file, calls the solve_sudoku method, and prints the results
def main(): 
    for i in range(1,6):
        #open the file and read the lines
        puzzle_id = "puzzle" + str(i) + ".txt"
        with open(puzzle_id, 'r') as file:
            lines = file.readlines()
        #Declare the puzzle data structure (list)
        puzzle = []
        #Go through each cell in the text file and assign the value to the puzzle[] list 
        for line in lines:
            row_values = [int(value) if value != '_' else None for value in line.strip().split()]
            puzzle.append(row_values)
        #Print the original puzzle
        print("Puzzle #" + str(i))
        print("Original Sudoku Puzzle: ")
        for row in puzzle:
            print(row)
        #Solve the puzzle and print the result if it exists
        if solve_sudoku(puzzle):
            print("\nFinished Sudoku Puzzle: ")
            for row in puzzle:
                print(row)
            print()
        else:
            #Print if there is no solution
            print("\nNo possible solution!")
            print()
#Call main
if __name__ == "__main__":
  main()