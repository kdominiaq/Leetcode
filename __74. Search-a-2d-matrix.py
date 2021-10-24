class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if target is between the first elements in rows, then search only in this row which was the first
        # varaibles 'j' and 'i' are responsible for iteration row by row to check is the target value is in the current row
        index_to_save = 0
        n = len(matrix)
        if n == 1:
            return True if target in matrix[0][::] else False
        
        # checking values between row <0, n-1>, than n = len(matrix[0])
        for i  in range(1, n):
            j = i - 1
            if target >= matrix[j][0] and target < matrix[i][0]:
                return True if target in matrix[j][::] else False
        
        # checking the last row, which hasn't been done yet
        return True if target in matrix[n - 1][::] else False    
