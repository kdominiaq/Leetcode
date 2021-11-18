class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        for num in nums:
            # if the number is not 0 then write it in the first index "left" and increase the value by one
            if num != 0:
                nums[left] = num
                left += 1
        
        while left < n:
            nums[left] = 0
            left += 1
