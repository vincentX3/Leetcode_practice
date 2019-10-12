# 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 <img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;">
 
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:
```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

## Solutions:
矩形面积=底x高，存在两个变量。
1. Brute-Force  
双重循环，O(n^2)，外层循环固定了底的左边，使双变量中的底变成递增。在内层循环中，我们只需要找到固定底左边时的最大面积；再通过外层循环来比较不同底边时的最大面积。  
上述是双重循环的意义，当然，我们实质上是暴力遍历了全部组合。
2. 双指针，移动“矮”的指针  
目标是去掉一层循环，实现O(n)的算法。承上所述，在两个变量下寻找最大面积是困难的，我们要想办法**固定一个变量**，或至少使其中一个变量**单调**变化。  
显然，底是容易固定的，我们使用`left`、`right`指向列表两端，两指针向内收缩时，底单调递减。  
再一步，思考指针如何移动。事实上，制约面积大小的，永远是**矮**的边，如同“木桶效应”。不断将“矮”边的指针向内收缩，比较新矩形的面积，即可得解。