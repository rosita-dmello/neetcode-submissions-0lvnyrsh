class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        cnt_zeros = 0
        for num in nums:
            if not num:
                cnt_zeros += 1
                continue
            else:
                product *= num

        result = [0] * len(nums)
        if cnt_zeros > 1:
            return result
        for i, num in enumerate(nums):
            if cnt_zeros:
                result[i] = 0 if num else product
            else:
                result[i] = product // num
        return result