class Solution:
    def maxArea(self, height: List[int]) -> int:
                
        step_water, most_water = 0, 0
        step_ele = 0
        # loop for loop to check every posible pair of value, 
        for itr_1, ele_1 in enumerate(height):
            for itr_2, ele_2 in enumerate(height):    
                # assign lowest value of the height, because height of the two clomun must be the same
                
                if ele_1 >= ele_2:
                    step_ele = ele_2
                else:
                    step_ele = ele_1
                    
                # calculating the value of area
                step_water = step_ele * (abs(itr_2 - itr_1))

                # checking value, if is grater, assign that
                if step_water > most_water:
                    most_water = step_water
                    itr_first, itr_last = itr_1, itr_2
                    
        return most_water
                        
