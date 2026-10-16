class Solution:
        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            n = len(matrix)
            m1 = len(matrix[0])

            l, r = 0, n * m1 - 1
            while l <= r:
                m = l + (r - l) // 2
                row, col = m // m1, m % m1
                if target > matrix[row][col]:
                    l = m + 1
                elif target < matrix[row][col]:
                    r = m - 1
                else:
                    return True
            return False


