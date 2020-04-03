# 75. Sort Colors

```
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
```

## Notes
1. 像题目中提示的那样，可以用3个桶来统计数组中0，1，2的个数，再依次赋值，复杂度为O(N^2)
2. 问题其实是经典的*Dutch national flag problem*（荷兰国旗问题），荷兰国旗从上至下依次为“红白蓝”，要将随机分布的红白蓝小球按照国旗颜色捋顺。  
   更泛化地说，问题讨论的是一个特殊的排序问题：给出两个key，将输入列表中元素按照与两个key的大小关系分为三组。  
   具体求解：
   使用3个指针：`red,white,blue`，使用白指针遍历列表。  
   当白指针指向元素为白(即nums[white]==1)时，该元素位置理想，无需变动，向前移动白指针；  
   当白指针指向元素为红(即nums[white]==0)时，将该元素与红指针指向元素交换，并向前移动红、白指针；  
   当白指针指向元素为蓝(即nums[white]==2)时，将该元素与蓝指针指向元素交换，并向后移动蓝指针。  