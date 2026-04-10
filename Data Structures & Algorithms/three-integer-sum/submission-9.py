class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1

            target = -n
            while j < k:
                sum_ = nums[j] + nums[k]
                if sum_ == target:
                    res.append([n, nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif sum_ < target:
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                else:
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return res

        