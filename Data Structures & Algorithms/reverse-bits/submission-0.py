class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(31):
            if n & 1:
                res += 1
                res <<= 1
            else:
                res <<= 1
            n >>= 1
        
        return res