class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break 
            if i > 0 and nums[i-1] == nums[i]:
                continue

            j = i+1
            k = len(nums) - 1

            while j < k:
                target = -(nums[i])
                sum_ = nums[j] + nums[k]
                if sum_ < target:
                    j+=1
                elif sum_ > target:
                    k-=1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -=1 
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return result
