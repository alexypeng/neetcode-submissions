class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            buckets[value].append(key)
        
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                k -= 1
                if k == 0:
                    return res