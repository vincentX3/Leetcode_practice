56. Merge Intervals
```
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
```

## Notes
审题，取最大相交区间。不要被输入样例误导了，题目**没有约束**输入样例中元素的大小顺序，需要自行处理。  

解法也是直观的，游标`left`,`right`记录当前区间的最值，若读入的`interval[0]`小于`right`，则并入区间，否则将此区间输出并更新游标。  
小细节，若直接对原输入`intervals`以`key=lambda x:x[0]`排序，更新游标时读入的`interval[1]`和`right`大小不定，应处理为`right=max(interval[1],right)`