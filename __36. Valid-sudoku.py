class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First Step
        # list of False, if digit is exist on the row, change value to True (index of list is digit -1), if one more time the same value will be found          (value on index will be True) return false, and stop the program
        # fox example ["5","3",".",".","7",".",".",".","."] will be 
        # [False, False, True, False, True, False, True, False, False]
        
        row_check = [False]*9
        for row in board:
            # checking the same digit in row
            for digit in row:
                if digit != '.':
                    digit = int(digit)
                    if row_check[digit - 1] == False:
                        row_check[digit - 1] = True
                    else:
                        return False
                
            row_check = [False]*9
        # Second Step
        # Checking columns, like the rows
        
        column_check = [False]*9
        for r in range(0,9):
            for c in range(0,9):
                if board[c][r] != '.':
                    if column_check[int(board[c][r]) - 1] == False:
                        column_check[int(board[c][r]) - 1] = True
                    else:
                        return False
            column_check = [False]*9
        
        # Third step
        # Checking squares
        row_index, col_index = 0, 0
        square_check = [False]*9

        for nb_of_squares in range(0,9):
            
            for r in range(0,3):
                for c in range(0,3): 
                    print(board[r+row_index][c + col_index])
                    if board[r+row_index][c + col_index] != '.':
                        if square_check[int(board[r+row_index][c + col_index]) - 1] == False:
                            square_check[int(board[r+row_index][c + col_index]) - 1] = True
                        else:
                            return False
            print(nb_of_squares,'----------------')
            if nb_of_squares == 2 or nb_of_squares == 5 or nb_of_squares == 8:
                row_index += 3

            if nb_of_squares == 2 or nb_of_squares == 5 or nb_of_squares == 8:
                col_index = 0
            else: 
                col_index += 3
                
            square_check = [False]*9
        return True
