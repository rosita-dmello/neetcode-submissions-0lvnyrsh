class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        c_min = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                c_min = min(nums[l], c_min)
            mid = l + ((r-l)//2)
            c_min = min(nums[mid], c_min)
            if nums[mid] >= nums[l]:
                l = mid+1
            else: 
                r = mid-1

        return c_min