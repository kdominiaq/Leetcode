class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # nb_of_ permutations is needed to multiply so must be 1        
        final_result = []
        step_result = []
        nb_of_permutations = 1
        
        # counting number of possible permutations        
        for i in range(1, len(nums) + 1):
            nb_of_permutations = nb_of_permutations * i 
        
        # if nums collects olny one element return [nums]
        if len(nums) == 1:
            return [nums]
        
        # firs loop iterations by nums, but the first element is skipped... the same situation, the first iteration must be skipped because programs firstly must add an element to the final result, then copy to step_result - if this block of code doesn't exist step_resylt will be always empty. 
        else:
            step_result = [[nums[0]]]
            for index_of_number, number in enumerate(nums[1:]):
                
                # copy final_result to step result and clear final_result 
                if not index_of_number == 0:
                    step_result = final_result.copy()
                final_result = []
                # loops will take the element from step_list, add one element in correct index to this list and add the new list to final_result, code must provide working not on reference object, so every time code must copy element to temporary varaible
                for ele in step_result:
                    for index in range(0, len(ele) + 1):
                        temp = ele.copy()
                        temp.insert(index, number)
                        final_result.append(temp)

            return final_result
