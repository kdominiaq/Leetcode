class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        
        s_len = len(s)
        
        # if letter from s is the in t increase the value by 1, becuase index_t will be the index of i list
        # if index_t == len(t) then return True, otherwise false
        index_s = 0
        for letter in t:
            if index_s >= s_len:
                return True
            if letter == s[index_s]:
                index_s += 1
                                
        if index_s == s_len:
            return True
        else:
            return False
