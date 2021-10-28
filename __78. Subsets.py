def solution(nums, lst):
    # run code if any element is in the list
    if len(nums) > 0:
        
        # append created list to final result, remeber to add copy list, becasue i next step the elements from the orginal list will be remove
        if not nums.copy() in lst:
            lst.append(nums.copy())
        
        # iteration element by element, run the function with skipped value
        for index in range(len(nums)):
            solution(nums[:index] + nums[index+1 :], lst)
            
        # remove the last item from the list
        del nums[len(nums) - 1]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        solution(nums, result)
        
        return result
