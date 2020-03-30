62. Unique Paths
```
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
```

## Notes
1. 很直观的，可以用二维dp数组求解，有` dp[i][j] = dp[i][j - 1] + dp[i - 1][j] `
2. 上述使用了`O(mn)`空间，我们发现实际上dp当前访问元素值，只由其左邻居和上一轮迭代的值决定，  
    进而可以优化空间，只用`O(n)`。  
    有，`dp[j]+=dp[j-1]`。