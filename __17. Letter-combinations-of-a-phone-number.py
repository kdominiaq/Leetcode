class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [[],
                  [],
                  ['a','b','c'],
                  ['d','e','f'],
                  ['g','h','i'],
                  ['j','k','l'],
                  ['m','n','o'],
                  ['p','q','r','s'],
                  ['t','u','v'],
                  ['w','x','y','z']]
        
        # if digis is empty return empty lsit
        if digits == '':
            return []     
        
        # if digits has only one digit return list form letter by id
        if int(digits) < 10:
            return letters[int(digits)]
        
        # create first layer of the digit and skip this  in while loop
        nb_of_itr = len(digits) 
        itr = 1
        final = letters[int(digits[0])]
        
        # take one digit and copy the final to final_step for creating another layer
        while itr != nb_of_itr:
            digit_per_step = int(digits[itr])
            final_step = final
            final = []
            for i in final_step:
                for j in letters[digit_per_step]:
                    final.append(i+j)
                    print(i+j)
            itr += 1
            
        return final              
   
