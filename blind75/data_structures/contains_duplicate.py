# https://leetcode-cn.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:  # return if there is dup in nums
        if not nums:
            return False
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False
