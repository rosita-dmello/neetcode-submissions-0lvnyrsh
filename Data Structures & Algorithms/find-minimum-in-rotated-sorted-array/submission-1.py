class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_ = nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                min_ = min(min_, nums[l])

            mid = l + ((r-l)//2)
            min_ = min(min_, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1 
            else:
                r = mid - 1
            
        return min_