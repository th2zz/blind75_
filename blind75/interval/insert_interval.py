import enum
from typing import List


class Solution:  # https://leetcode.cn/problems/insert-interval/
    """https://mp.weixin.qq.com/s/ioUlNa4ZToCrun3qb4y4Ow
Insert newInterval into intervals such that 

1. intervals is still sorted in ascending order by starti 

2. intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find insert pos: the first interval s.t. interval.start <= newInterval.start, merge overlapping intervals if necessary
        res = []
        i = 0
        # append all non-overlapping intervals
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # now interval.end >= newInterval.start  e.g. [2,4] [3,5] or [2,4] [4,5]
        # still overlapping: construct new interval by merging consecutive overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)
        # at this point, i is at a non-overlapping interval
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
