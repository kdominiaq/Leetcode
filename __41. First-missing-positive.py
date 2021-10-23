class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # check if list has only one element:
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            elif nums[0] > 1:
                return 1
        
        # values of the nums in ths list in the index, so if nums = [0,3], list_of_index = will be like this [True, Fasle, True, False]
        lowest_exist_value = [0]*2
        for number in nums:
            if number >= 0:
                # add as many filds in list as is nessesery to save the number Value, !!! number value  - 1 = index !!! (becasue indexes in the liast are from 0, and the 0 isn't a postive value)
                    lowest_exist_value = lowest_exist_value + [0]*(abs(len(lowest_exist_value) - number))
                    lowest_exist_value[number - 1 ] = 1
        print(lowest_exist_value)        
        # if value of the index is 0, than return index becasue the value doesn;t exist 
        for index, value in enumerate(lowest_exist_value):
            if index == 0 and value == 0:
                return  1
            elif value == 0:
                return index + 1
