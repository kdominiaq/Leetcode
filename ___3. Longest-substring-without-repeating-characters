class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_counter = 0
        
        nonrepeating_letters =[]

        for letter in s:
            # adding letter if is not existed in list
            if letter not in nonrepeating_letters:
                nonrepeating_letters.append(letter)
                
            # removing the letter from the first element until the detected letter which has been repeating
            else:
                while True:
                    if nonrepeating_letters:
                        checked_letter = nonrepeating_letters[0]
                        nonrepeating_letters.pop(0)  

                        if checked_letter == letter:
                            break
                # add the repeated letter to the end of the list
                nonrepeating_letters.append(letter) 
            
            # checking lenght of substring and save the letter
            if longest_substring_counter < len(nonrepeating_letters):
                longest_substring_counter = len(nonrepeating_letters)

        return longest_substring_counter
