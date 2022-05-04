class Solution:  # https://leetcode-cn.com/problems/container-with-most-water/
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:  # always move the pillar with smaller height, only this way we can have larger area
                l += 1
            else:
                r -= 1
        return ans
