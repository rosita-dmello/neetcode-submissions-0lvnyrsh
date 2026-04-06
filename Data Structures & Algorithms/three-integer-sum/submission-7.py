class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        result = []
        nums.sort()
        for num in nums:
            count[num] += 1
        
        for i, a in enumerate(nums):
            count[a] -= 1
            if a > 0:
                break
            if i > 0 and nums[i-1] == a:
                continue
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j > i+1 and nums[j] == nums[j-1]:
                    continue 
                target = -(a + nums[j])
                if target in count and count[target] > 0:
                    result.append([a, nums[j], target])
            for j in range(i+1, len(nums)):
                count[nums[j]] +=1
        return result
