class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                bar = stack.pop()
                area = (i - bar[0]) * bar[1]
                max_area = max(max_area, area)
                start = bar[0]
            stack.append((start, h))

        while stack:
            bar = stack.pop()
            area = (len(heights) - bar[0]) * bar[1]
            max_area = max(max_area, area)
        return max_area