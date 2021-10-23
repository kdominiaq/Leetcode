class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # varaible for saving actual index of the list where can save value which is not equal to val 
        index = 0
        
        # iteration by every values, if value is note equel to val save this value in list by index, and increase index value by 1, if not skip this value
        for itr in range(len(nums)):
            if nums[itr] != val:
                nums[index] = nums[itr]
                index +=1
        return index
