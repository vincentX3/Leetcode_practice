# 55. Jump Game

```
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

```

## Notes

给出3种思路，第一种最直接但低效，第二、三种基于第一种优化，思路相近，理解一种即可。

1. 暴力模拟
对于一条`length=n`的路，直接声明`list path[n]`，初始化元素值为0，遍历`nums`数组来填充`path`。具体的，将`path[i+1:i+num]`元素值皆设为1.
当`path[-1]==1`时返回`True`。

2. 基于上述情况深入思考：我们不需要一个`path`来记录每个点是否可达，事实上，可达的点为`[0:max_jump_length]`，所以，只需要研究`max_jump_length`即可。  
具体而言，遍历`nums`，当当前点可达时（`i<=max_jump_length`），更新`max_jump_length = max(max_jump_length, i+nums[i])`  
当`max_jump_length>= len(nums)`时，可以跳到终点。

3. 从终点回退。