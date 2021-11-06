class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        
        for i in range(32):
            # shift bit to left by 1
            m = m << 1
            
            # if bit from the 'n' is 1, add '1' to the last index of 'm' & is logic AND
            if n & 1 == 1:
                m += 1
            
            #shift bit to right by 1 bits
            n = n >> 1
            
        return m
