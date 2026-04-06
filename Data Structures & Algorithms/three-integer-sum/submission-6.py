class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        soln = []
        
        for i in range(len(nums)):
            target = 0 - nums[i]
            j = i+1
            k = len(nums) - 1
            if i> 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                sum_ = nums[j] + nums[k]
                if sum_ == target:
                    soln.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1  
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif sum_ < target:
                    j +=1                  
                else:
                    k -=1
                    

        return soln