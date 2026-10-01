class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k):
            elapsed = 0
            for pile in piles:
                elapsed += -(-pile // k)
            return elapsed <= h


        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            m = l + (r-l) // 2

            print(m)
            print(can_eat(m))

            if can_eat(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res