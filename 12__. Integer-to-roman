class Solution:
    def intToRoman(self, num: int) -> str:
        number_roman = ''
        
        numbers_for_one = ['I','X','C','M']
        numbers_for_dic = ['X','C','M']
        numbers_for_half_dic = ['V', 'L', 'D']
        
        itr = 0
        while num:
            num_step = num % 10
            num = int(num / 10)
            
            
            if num_step == 1:
                number_roman = numbers_for_one[itr] + number_roman 
            elif num_step == 2:
                number_roman = numbers_for_one[itr] + numbers_for_one[itr] + number_roman
            elif num_step == 3:
                number_roman = numbers_for_one[itr] + numbers_for_one[itr] + numbers_for_one[itr] + number_roman
            elif num_step == 4:
                number_roman = numbers_for_one[itr] + numbers_for_half_dic[itr] + number_roman
            elif num_step == 5:
                number_roman = numbers_for_half_dic[itr] + number_roman
            elif num_step == 6:
                number_roman = numbers_for_half_dic[itr] + numbers_for_one[itr] + number_roman
            elif num_step == 7:
                number_roman = numbers_for_half_dic[itr] + numbers_for_one[itr] + numbers_for_one[itr] +number_roman
            elif num_step == 8:
                number_roman = numbers_for_half_dic[itr] + numbers_for_one[itr] + numbers_for_one[itr] + numbers_for_one[itr] + number_roman
            elif num_step == 9:
                number_roman = numbers_for_one[itr] + numbers_for_dic[itr] + number_roman
            
            

            itr += 1
            
        return number_roman
