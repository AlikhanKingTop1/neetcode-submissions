class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 > nums2:
            nums2,nums1 = nums1,nums2
        
        total= len(nums1) + len(nums2)
        half = (total+1)//2

        l = 0
        r = len(nums1)
        A = nums1
        B = nums2
        while l<=r:
            i = (r+l) // 2
            j = half - i
            
            Aleft = A[i-1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j-1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total %2 == 1:
                    return max(Aleft,Bleft)
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i+1