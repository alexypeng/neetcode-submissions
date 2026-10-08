class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        total_len = len(A) + len(B)
        half_len = total_len // 2

        if len(B) < len(A):
            A, B = B, A

        l = 0
        r = len(A) - 1

        while True:
            i = l + (r - l) // 2
            j = half_len - i - 2

            A_left_end = A[i] if i >= 0 else float('-inf')
            A_right_start = A[i+1] if i+1 < len(A) else float('inf')

            B_left_end = B[j] if j >= 0 else float('-inf')
            B_right_start = B[j+1] if j+1 < len(B) else float('inf')

            if A_left_end <= B_right_start and B_left_end <= A_right_start:
                return min(B_right_start, A_right_start) if total_len % 2 else (max(A_left_end, B_left_end) + min(A_right_start, B_right_start)) / 2

            elif A_left_end > B_right_start:
                r = i - 1
            else:
                l = i + 1





