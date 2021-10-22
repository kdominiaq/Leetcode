import re

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # first word will be the pattern for search, rest will be string re.search(pattern, string, flags=0)
        search_word = strs[0]
        len_s = len(search_word)
        
        # varaibles for saving the vounter and longest prefix
        longest_prefix = ""
        longest_prefix_counter = 0
        
        # searching prefix in all word, if one of the words hasn't got pattern, break the loop and go for next pattern
        # generating the pattern like [0:], [0:-1], [0:-2] ... 
        for letter in reversed(range(0, len_s + 1)):   
            to_check = search_word[0:letter]
            print(to_check)
            for word in strs[1:]:
                print(to_check, word)
                if not re.search(to_check, word[0:letter]):
                    
                    to_check = ""
                    break
            if len(to_check) >  longest_prefix_counter:
                longest_prefix = to_check
                longest_prefix_counter = len(to_check)
                    
        return longest_prefix
                
