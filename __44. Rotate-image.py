class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Define variables
        matrix_len = len(matrix)
        rotate_image  = [[0 for i in range(matrix_len)] for j in range(matrix_len)]
        
        # save layer by layer to the last values in lists
        for i in range(matrix_len):
            for j in range(matrix_len):
                rotate_image[j][matrix_len - 1 - i] =  matrix[i][j] 
        
        matrix = rotate_image
