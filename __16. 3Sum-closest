class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        collecting_sum_lists = []
        smallest_difference  = int()
        closest_to_target = int()
       
        def Solution(numbers, collecting_list):
            while len(numbers) >= 3:
                
                for itr, number in enumerate(numbers):
                    if itr == 0:
                        continue
                    else:
                        result = numbers[:itr] + numbers[itr + 1:]
                        Solution(result, collecting_list)
                
                if len(numbers) == 3:
                    sum_of_prepared_list = sum(numbers)
                    collecting_list.append(sum_of_prepared_list)
                    print(sum_of_prepared_list)
                numbers.pop(0)
                    
        Solution(nums, collecting_sum_lists)

        for itr, digit in enumerate(collecting_sum_lists):
            if itr == 0:
                closest_to_target = digit
            if abs(digit - target) < smallest_difference:
                smallest_difference = abs(digit - target)
                closest_to_target = digit
                
        return closest_to_target
