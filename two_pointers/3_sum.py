# https://leetcode-cn.com/problems/3sum/
class Solution:  # return all triplets (value) that 3 sum to 0, can have duplicates
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):  # fix starting point
            if i > 0 and nums[i] == nums[i - 1]:  # skip repeated starting point
                continue
            self.find_two_sum_unique_pair(nums=nums, start_idx=i + 1, target=-nums[i], result=result)
        return result

    def find_two_sum_unique_pair(self, nums, start_idx, target, result):
        start, end = start_idx, len(nums) - 1
        while start < end:
            sum = nums[start] + nums[end]
            if sum == target:
                result.append([-target, nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif sum < target:
                start += 1
            elif sum > target:
                end -= 1
