#1 use numpy
import numpy as np

A = [[1,2], [3,4]]
An = np.array(A)
A_anti_90 = np.rot90(A)
print A_anti_90
A_clock_90 = np.rot90(A, k=-1)
print A_clock_90


#2 use class

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == []:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in xrange(left, right + 1):
                result.append(matrix[top][j])
            for i in xrange(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(xrange(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(xrange(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result


if __name__ == "__main__":
    print Solution().spiralOrder([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]])
    print Solution().spiralOrder([[2, 3]])