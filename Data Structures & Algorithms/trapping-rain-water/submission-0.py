class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        lg_pre = 0
        for i in range(0, len(height)):
            prefix[i] = lg_pre
            lg_pre = max(lg_pre, height[i])

        lg_suf = 0
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = lg_suf
            lg_suf = max(lg_suf, height[i])

        area = 0
        for i in range(len(height)):
            area_i = min(prefix[i], suffix[i]) - height[i]
            if area_i > 0:
                area += area_i
        return area
        



