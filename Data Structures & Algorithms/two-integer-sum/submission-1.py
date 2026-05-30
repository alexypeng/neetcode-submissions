class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(int)

        for i, num in enumerate(nums):
            want = target - num
            if want in indices:
                return [indices[want], i]
            indices[num] = i