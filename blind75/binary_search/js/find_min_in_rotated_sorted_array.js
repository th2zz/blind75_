/**
 * @param {number[]} nums
 * @return {number}
 */
 var findMin = function (nums) {
    if (!nums.length) {
        return -1;
    }
    let start = 0, end = nums.length - 1;
    while (start + 1 < end) {
        let mid = Math.floor((start + end) / 2);
        if (nums[mid] > nums[end]) {
            start = mid;
        } else {
            end = mid;
        }
    }
    return Math.min(nums[start], nums[end]);
};