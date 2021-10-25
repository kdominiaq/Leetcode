class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #             right,  down,    left,    up  
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),]
        # if the last element will on the end of the row, column or eqauels to 0 than turn right, to do it the previous turn must be checked
        nb_of_col, nb_of_row = len(matrix), len(matrix[0])
        
        #start is the indexes of the first element in matrix, next by goes to right
        x, y = 0, 0
        
        # go to right 
        dx, dy = (0, 1)
        # counting numbers of steps, which must be <= nb_of_col * nb_of_row
        counter = 0
        final_counter = nb_of_col * nb_of_row
        
        # every time when the next step can't be found, increase this value, module counting the itaration for directions
        iteration_by_directions = 0
        result = []
        # every time while turn will be done, the code must check next value and possibily of turn, if the value is 0 or next step will be out of range in matrix, than must be turn (change the diractions)
        while counter < final_counter:
           
            result.append(matrix[x][y])
            matrix[x][y] = 0
            if x + dx  >= 0 and x + dx < nb_of_col and y + dy >= 0 and y + dy < nb_of_row and matrix[x+dx][y+dy] != 0:
                x += dx
                y += dy
            else:
                iteration_by_directions += 1
                dx, dy = directions[iteration_by_directions % 4]
                x += dx
                y += dy

            counter += 1 
            
        return result
