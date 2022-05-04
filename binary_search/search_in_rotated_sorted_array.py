# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

class Solution:  # search for target in rotated sorted prefix_array O(logn), return index of target or -1 if not present
    def search(self, nums: List[int], target: int) -> int:  # assume left rotate
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[len(nums) - 1]:  # on smaller half (right half)   # TODO 这里必须严格这样写
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:  # on larger half (left half)
                if nums[start] <= target <= nums[mid]:  # target is in interval [nums[start] ... nums[mid]]
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
