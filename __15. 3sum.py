class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # if nums doesn't contain 3 values
        if len(nums) < 3:
            return []
        else:
            for itr_i, ele_i in enumerate(nums):
                 for itr_j, ele_j in enumerate(nums):
                    for itr_k, ele_k in enumerate(nums):
                        
                        # indexes can not be the same
                        if itr_i != itr_j and itr_i != itr_k and itr_j != itr_k:
                            
                            # cheking if addition of values is equel to 0 
                            if (ele_i + ele_j + ele_k) == 0:
                                result_step =  [ele_i, ele_j, ele_k]
                                is_dupicate = False
                                result_step.sort()
                                
                                # add if list is empty, next time check if sumof3 has already existed
                                if result == []:
                                    result.append(result_step)
                                else:
                                    for ele in result:
                                        if result_step == ele:
                                            is_dupicate = True
                                            break
                                    
                                    if not is_dupicate: 
                                         result.append(result_step)
                                    
        return result
