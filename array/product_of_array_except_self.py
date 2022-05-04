# https://leetcode-cn.com/problems/product-of-array-except-self/
# return arr: arr[i] = product of all elements except nums[i], O(n) TIME with no division operation
class Solution:
    def productExceptSelf1(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        forward_prefix_product = [1] * len(nums)  # prefix product before pos i (not include i)
        backward_prefix_product = [1] * len(nums)  # prefix product (backward) after pos j (not include j)
        for i in range(1, len(nums)):
            forward_prefix_product[i] = forward_prefix_product[i - 1] * nums[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            backward_prefix_product[j] = backward_prefix_product[j + 1] * nums[j + 1]
        res = [1] * len(nums)  # product of all nums except self init: all 1
        for i in range(len(nums)):
            res[i] *= forward_prefix_product[i] * backward_prefix_product[i]
        return res

    # def productExceptSelf1(self, nums: list[int]) -> list[int]:
    #     if not nums:
    #         return []
    #     # prepare forward and backward prefix product array, (including self)
    #     forward_prefix_product = [1] * len(nums)  # prefix product up to and including pos i
    #     backward_prefix_product = [1] * len(nums)  # prefix product (backward) up to and including pos j
    #     forward_prefix_product[0], backward_prefix_product[len(nums) - 1] = nums[0], nums[len(nums) - 1]
    #     for i in range(1, len(nums)):
    #         forward_prefix_product[i] = forward_prefix_product[i - 1] * nums[i]
    #     for j in range(len(nums) - 2, -1, -1):
    #         backward_prefix_product[j] = backward_prefix_product[j + 1] * nums[j]
    #     # print(forward_prefix_product)
    #     # print(backward_prefix_product)
    #     res = [1] * len(nums)  # product of all nums except self init: all 1
    #     for i in range(len(nums)):
    #         if i >= 1:
    #             res[i] *= forward_prefix_product[i - 1]
    #         if i <= len(nums) - 2:
    #             res[i] *= backward_prefix_product[i + 1]
    #     return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):  # use res as placeholder for forward prefix product before pos i
            res[i] = nums[i - 1] * res[i - 1]
        R = 1  # traverse backward and use 1 variable for backward prefix product after j
        for i in reversed(range(len(nums))):  # this save the space for second prefix array
            res[i] = res[i] * R
            R *= nums[i]  # prepare backward prefix product after j for next round
        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
