class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)

        while l < r:
            mid = l + (r - l) // 2

            if matrix[mid][0] > target:
                r = mid
            else:
                l = mid + 1
        
        arr = matrix[r-1]
        print(arr)

        l = 0
        r = len(arr)

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False