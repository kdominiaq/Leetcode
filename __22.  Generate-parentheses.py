class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # now my solution, but realy good recuration example
        output = []
        
        def rec(left, right, stack, cand):
            # If the number of left and right side of the brackets is equal to 0, add this solution to the output
            if left == right == 0:
                output.append(cand)
                return
            
            # cheking if left brackets exist, if is decreasing number of left brackets, and add +1 to stack, so it means, at least one left brackets is waiting for right brackets
            if left > 0:
                rec(left -1, right, stack +1, cand + "(")

            # same situation like upper, but now we must chank also stack value if it's 0 that means none left brackets is waiting for close
            if right > 0 and stack > 0:
                rec(left, right - 1, stack-1,cand+ ")")
                
        rec(n ,n, 0, "")
            
        return output   
