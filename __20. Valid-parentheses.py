class Solution:
    def isValid(self, s: str) -> bool:
        # variable 
        s = list(s)
        previos_remove = True

        # checking if counter of the brackets are odd
        if len(s) % 2 != 0:
            return False
        
        else:
            # checking previos iteration, if none of if statment happend stop thwe while, bbecasue anything in "s" is the pair of brackets
            while previos_remove:
                previos_remove = False
                
                for itr, _ in enumerate(s):
                    if itr != 0:
                        if s[itr - 1] == '{'and s[itr] == '}':
                            s.pop(itr - 1)
                            s.pop(itr - 1)
                            previos_remove = True
                        elif s[itr - 1] == '('and s[itr] == ')':
                            s.pop(itr - 1)
                            s.pop(itr - 1)
                            previos_remove = True
                        elif s[itr - 1] == '['and s[itr] == ']':
                            s.pop(itr - 1)
                            s.pop(itr - 1)
                            previos_remove = True

            if len(s) == 0:
                return True
            else:
                return False
