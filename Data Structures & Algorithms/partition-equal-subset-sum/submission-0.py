class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            temp = set()

            for num in dp:
                if num + nums[i] == target:
                    return True
                temp.add(num)
                temp.add(num + nums[i])
            dp = temp
        return False
            

