#88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

> Input:  
nums1 = [1,2,3,0,0,0], m = 3  
nums2 = [2,5,6],       n = 3  
> 
>output: [1,2,2,3,5,6]

---
## Solution:
1. 暴力“插拔”
思路简单粗暴，两数组元素比较，当待插入数组的元素大于容器数组元素时，直接`insert()`之。  
由于要求容器数组长度不变，再对容器数组`pop()`。
> 不过……效率低的可怕，效率位列倒数30%
2. Merge sorted like
像归并排序一般，本题只需利用容器数组尾端的空前空间，对有效数据段从大到小进行归并排序即可。
结果相当喜人，开心一下☺。
![ranking result](88MergeSortedArray.png)
