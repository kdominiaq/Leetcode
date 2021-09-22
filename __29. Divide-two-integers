class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        value = 0

        # save '-' sign dividend
        sign_dividend = str(dividend)[0]
        if sign_dividend == '-':
            dividend = int(str(str(dividend)[1:]))
        
        # save '-' sign dividend
        sign_divisor = str(divisor)[0]
        if sign_divisor == '-':
            divisor = int(str(str(divisor)[1:]))

        # change after itr is the same like divisor
        changed_divisor = divisor
        
        # check if divisor = 1 or -1
        if divisor == 1:
            # check sign of result, if double '-', final result is positive
            if sign_dividend == '-' and sign_divisor == '-':
                return dividend
            elif sign_dividend != '-' and sign_divisor != '-':
                return dividend
            elif sign_dividend == '-' and sign_divisor != '-':
                return int(sign_dividend + str(dividend))
            elif sign_dividend != '-' and sign_divisor == '-':
                return int(sign_divisor+ str(dividend)) 

        # every time if itr is equel to iteration +1 to value
        for itr in range(1, dividend + 1):
            if itr == changed_divisor:
                value += 1
                changed_divisor += divisor
        
        
        
        # check sign of result, if double '-', final result is positive
        if sign_dividend == '-' and sign_divisor == '-':
            return value
        elif sign_dividend != '-' and sign_divisor != '-':
            return value
        elif sign_dividend == '-' and sign_divisor != '-':
            return int(sign_dividend + str(value))
        elif sign_dividend != '-' and sign_divisor == '-':
            return int(sign_divisor+ str(value))
        
