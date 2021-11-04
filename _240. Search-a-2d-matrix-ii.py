class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            # return count of value which is lower than a given target. Remember to protect the out-of-range exception because the function can return a value which is greater than it. 
            d = bisect.bisect_left(row, target)
            if d < len(row):
                # checking only value which is given by bisect fucntion
                if row[d] == target:
                    return True
