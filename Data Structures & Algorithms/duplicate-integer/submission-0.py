class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDup = False
        numDuplicates = {}
        for i in nums:
            if numDuplicates.get(i, None) is not None:
                hasDup = True
                break
            else:
                numDuplicates[i] = True
        return hasDup
