class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if first fit word is found save indexes of start and end
        start_find, end_find = False, False
        start_index, end_index = -1, -1
        
        # checking if list nums has only one vale and values is the same like target
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        
        # first digit which is the same like taget save to satart_index, next digit )of course if exists) save to end index
        for itr, digit in enumerate(nums):
            if digit == target and start_find == False:
                start_index = itr
                end_index = itr
                
                start_find = True
                end_find = True
            elif end_find and digit == target:
                end_index = itr

        return [start_index, end_index]
