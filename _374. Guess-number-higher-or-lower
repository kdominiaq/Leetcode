# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        number_mid_low = round(n / 3)
        number_mid_high = round(n * 2 / 3)
        while guess(number_mid_low) != 0 or guess(number_mid_high) != 0:
            
            number_mid_low += guess(number_mid_low)
            number_mid_high += guess(number_mid_high)
        # return A+1 if A > B else A-1
        return number_mid_high if number_mid_high == 0 else number_mid_low
