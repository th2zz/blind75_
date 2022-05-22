from typing import List
import heapq

class Solution:
    # 判断区间是否无重叠  (判断能否参加所有会议)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])
        if not sorted_intervals:
            return True
        for i in range(1, len(sorted_intervals)):
            interval = sorted_intervals[i]
            prev_interval = sorted_intervals[i - 1]
            if prev_interval[1] > interval[0]:  # [1, 2] [2,3] not counted as overlap
                return False
        return True

    # return min# meeting rooms to accommodate all meetings
    def minMeetingRooms(self, intervals: List[List[int]]):
        intervals.sort(key=lambda x:x[0])  # sort by start time
        earliest_endtimes: list[int] = [intervals[0][1]]  # init heap with first item
        ans = 1
        for i in range(1, len(intervals)):  # traverse remaining intervals; heap[0] = peeek!
            interval = intervals[i]
            if interval[0] < earliest_endtimes[0]: # conflict 会议开始时间 < 最早结束时间，需增加会议室
                ans+=1
            else: # no conflict 可以在最早结束的会议之后开始当前会议，之前的最早结束时间变成当前会议结束的时间
                heapq.heappop(earliest_endtimes) 
            heapq.heappush(earliest_endtimes, interval[1])
        return ans   
