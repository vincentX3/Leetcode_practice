class Solution:
    def merge_v1(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        ans = []
        l, r = intervals[0]
        for interval in intervals[1:]:
            if r >= interval[0]:  # overlap
                r = max(interval[1], r)
            else:
                ans.append([l, r])
                l, r = interval
        ans.append([l, r])
        return ans

    def merge_v2(self, intervals: List[List[int]]) -> List[List[int]]:
        # from Leetcode, more elegant and concise
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    def merge_v3(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        if len(intervals) == 1:
            return intervals
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        starts.sort()
        ends.sort()
        ans, j, length = [], 0, len(starts)
        for i in range(length):
            if i == length - 1 or starts[i + 1] > ends[i]:
                # end of overlap
                ans.append([starts[j], ends[i]])
                j = i + 1
        return ans
