class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        soln = set()
        
        for i in range(len(nums)):
            target = 0 - nums[i]
            j = i+1
            k = len(nums) - 1
            while j < k:
                sum_ = nums[j] + nums[k]
                if sum_ == target:
                    soln.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    j+=1
                    k-=1
                elif sum_ < target:
                    j +=1
                else:
                    k -=1
        result = []
        print(result)
        for a,b,c in soln:
            result.append([a,b,c])

        return result