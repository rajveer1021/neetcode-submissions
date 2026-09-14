class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2

            m = mid // cols
            n = mid % cols

            if matrix[m][n] == target:
                return True

            elif matrix[m][n] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False