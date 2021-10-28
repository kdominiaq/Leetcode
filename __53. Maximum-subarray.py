# Cubic Time To Kadane's Algorithm 
# https://www.youtube.com/watch?v=2MmGzdiKR9Y&ab_channel=BackToBackSWE
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = []
        
        for itr, ele in enumerate(nums):
            if itr == 0:
                result.append(ele)
            else:
                result.append(max(nums[itr], nums[itr] + result[itr - 1]))
                        
        return max(result)
