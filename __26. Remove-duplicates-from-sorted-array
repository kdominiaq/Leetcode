class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # saving index of checked value
        index = 0
        
        # loop start from 1 because code will check equals of the next values
        for itr in range(1, len(nums)):
            
            # is values are not the same, add value to list nums, and increase index value for check another element in next iteration
            if nums[index] != nums[itr]:
                index += 1
                nums[index] = nums[itr]
        # it's nessesry to increase value by 1 becasue the index varaible start form 0, but 0 is one element        
        return index + 1
