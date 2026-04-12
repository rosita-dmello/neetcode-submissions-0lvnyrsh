class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A,B = B,A
        
        n = len(A) + len(B)
        half = n//2
        l = 0
        r = len(A) - 1

        while True:
            m1 = l + ((r-l)//2)

            m2 = half - (m1+1) - 1

            Aleft = A[m1] if m1 >= 0 else float("-infinity")
            Bleft = B[m2] if m2 >= 0 else float("-infinity")
            Aright = A[m1+1] if m1+1 < len(A) else float("infinity")
            Bright = B[m2+1] if m2+1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if n%2:
                    return min(Aright, Bright)
                else:
                    return ((max(Aleft, Bleft) + min(Aright, Bright))/2)
            elif Aleft > Bright:
                r = m1 - 1
            else:
                l = m1+1