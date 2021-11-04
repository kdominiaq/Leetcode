class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initialization variables for the first and the last  element from row
        first_index = 0
        last_index = len(matrix[0]) - 1
        
        # if target value is found "is_found" will be True
        is_found = False
        
        for row in matrix:
            # checking the first element and the last from the row, if target is between both values search this row for element
            if target >= row[first_index] and target <= row[last_index]:
                # if row contains target value, return true
                is_found = True if target in row else None
                
        return is_found
