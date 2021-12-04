class Solution:
    def left_right_search(self, nums: List[int], right_index: int, left_index: int,  target: int) -> bool:
        """
        Take an array of nums and find the target value, every step the array will be decreased by one value from the right and left side.  
        """
        
        while right_index <= left_index:

            if nums[right_index] == target or nums[left_index] == target:
                return True

            right_index += 1
            left_index -= 1
            
        return False
        
        
    
    def search(self, nums: List[int], target: int) -> bool:
        # take a look for the first and last numbers in array
        
        first_num = nums[0]
        last_num = nums[-1]
        
        if first_num == target:
            return True
        
        if last_num == target:
            return True
        
        
        # divide the array into two arrays, by check the ranges from (first_nume, middle_num> and (middle_num, last_num>
    
        middle_index = int((len(nums))/2)
        middle_num = nums[middle_index]
        
        # (first_num, middle_num>
        
        if target > first_num and target <= middle_num:
            print("left")
            return self.left_right_search(nums, 0, middle_index, target)
            
        
        
        # <middle_num, last_num)
        elif target < last_num and target >= middle_num:
            print("right")
            return self.left_right_search(nums, middle_index, len(nums) - 1, target)
            
        # exception
        # nums: [1,0,1,1,1]
        # target: 0
        else:
            return self.left_right_search(nums, 0, len(nums) - 1, target)
