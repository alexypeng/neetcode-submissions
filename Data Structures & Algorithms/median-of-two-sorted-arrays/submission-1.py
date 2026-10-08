class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            A_idx = (l + r) // 2
            B_idx = half - A_idx - 2

            A_left = A[A_idx] if A_idx >= 0 else float('-inf')
            A_right = A[A_idx + 1] if (A_idx + 1) < len(A) else float('inf')

            B_left = B[B_idx] if B_idx >= 0 else float('-inf')
            B_right = B[B_idx + 1] if (B_idx + 1) < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                return (max(A_left, B_left) + min(B_right, A_right)) / 2 if total % 2 == 0 else min(A_right, B_right)
            elif A_right > B_left:
                r = A_idx - 1
            else:
                l = A_idx + 1