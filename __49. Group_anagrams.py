class Solution:   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert word to the sum of the letter, nut firsty convert char to ascii number 
        # example: ["eat","tea","tan","ate","nat","bat"]
        # result: {314: ['eat', 'tea', 'ate'], 323: ['tan', 'nat'], 311: ['bat']}
        dict_of_counted_words = {}
        
        for word in strs:
            sum_of_ascii = 0
            for letter in word:
                sum_of_ascii = sum_of_ascii + ord(letter)
            
            if not sum_of_ascii in dict_of_counted_words:
                dict_of_counted_words[sum_of_ascii] = []
                
            dict_of_counted_words[sum_of_ascii].append(word)
        
        return list(dict_of_counted_words.values())
