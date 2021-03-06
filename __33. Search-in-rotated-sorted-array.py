class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # if value if between the first and the end value return -1, because it's not posibble to exist this value in that list
        if target < nums[0] and target > nums[-1]:
            return -1
        
        if len(nums) == 1 and nums[0] != target:
            return -1
        
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        if target > nums[0]:
            for itr, value in enumerate(nums):
                # for the first element, provide the exeception "out of the range"
                if itr == 0 and target == value:
                    return itr
                
                # normal cheking, if value exisstreturn index
                elif target == value:
                    return itr
                
                # if value is between values which are next of theses return -1, it means value doesn't exist in thgre list nums
                elif nums[itr - 1] < target and nums[itr] > itr:
                    return -1
                else:
                    return -1
                
        elif target < nums[-1]:

            for itr, value in enumerate(reversed(nums)):
                # for the first element, provide the exeception "out of the range"
                if itr == 0 and target == value:
                    return len(nums) - itr - 1
                
                # normal cheking, if value exisstreturn index
                elif target == value:
                    return len(nums) - itr - 1
                
                # if value is between values which are next of theses return -1, it means value doesn't exist in thgre list nums
                elif nums[itr - 1] < target and nums[itr] > itr:
                    return -1
                
                else:
                    return -1 
