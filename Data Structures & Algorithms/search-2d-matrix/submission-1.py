class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l+r) // 2
            left_m = matrix[m][0]
            right_m = matrix[m][-1]
            l_ptr = 0
            r_ptr = len(matrix[m]) -1
            if left_m <= target <= right_m:
                
                    while l_ptr <= r_ptr:
                        m_ptr = (l_ptr+r_ptr) // 2
                        if matrix[m][m_ptr] == target:
                           return True
                        elif matrix[m][m_ptr] > target:
                            r_ptr = m_ptr - 1
                        elif matrix[m][m_ptr] < target:
                            l_ptr = m_ptr + 1
                    return False
            elif left_m > target:
                r = m-1
            elif right_m < target:
                l = m+1
        return False