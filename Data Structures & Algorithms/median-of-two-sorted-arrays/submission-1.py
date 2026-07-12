class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = []
        new_arr.extend(nums1)
        new_arr.extend(nums2)
        new_arr = sorted(new_arr)
        if len(new_arr) % 2 == 1:
            return float(new_arr[len(new_arr)//2])
        else:
            mid = len(new_arr) // 2
            mid2 = mid - 1
            sum_med = (new_arr[mid]+new_arr[mid2]) / 2
            return sum_med