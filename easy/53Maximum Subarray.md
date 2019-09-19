#53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

> Input: [-2,1,-3,4,-1,2,1,-5,4],  
Output: 6  
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

---
## solution
1. O(n),单趟遍历，分析产生最大值的情形，用2个变量维护  
似乎曾经碰到过此题，有大致印象，算法思路如下：  
设有两个变量，**最大子列和**`maximum`，及**当前子列和**`curr_total`。  
大家思考下，
遍历列表时，我们期望通过维护`curr_total`，试探**当前**子列和能得到的**最值**是否能大于'maximum'。  
那，是不是只有在`curr_total>=0`时，才有机会由于叠加后继子列，成为`maximum`？  
好比说，`curr_total=2`，下一个元素`num[i+1]=-5`，`num[i+2]=4`,显然加上`num[i+1]`后的`curr_total`，小于`curr_tota=num[i+2]`。
那我们遇到`curr_total+num[i+1]<0`时，直接**reset**`curr_total=0`不就成了？
别想得太简单了，还要考虑只有1个元素的情况，及与list里面全是负数的情况。

2. **divide&conquer**
其实没想出来，感谢[**@lucifer**](https://github.com/azl397985856)的图例解读,引用记录如下。
![divide_and_conqer](https://github.com/azl397985856/leetcode/blob/master/assets/problems/53.maximum-sum-subarray-divideconquer.png)