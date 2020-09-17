# Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ *n* (*n* = size of array), some elements appear **twice** and others appear **once**.

Find all the elements that appear **twice** in this array.

Could you do it **without extra space and in O(*n*) **runtime?



**Example:**

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```



# Solution

Since we have to solve it without extra space, we should make better use of existing vector `nums`.  

Because all the number are:  $1 ≤ a[i] ≤ n (n = size of array)$, which means we could get [1, 2, ..., n] at most (without duplicate). So we could use index of array to record status.

Specifically, we mark the content of index to be negative, e.g. we got `3`, then we have `idx=3`, we make `nums[idx] *= -1`. So every time we encounter a negative number, we know that the index of it have been seen.

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        duplicate = []
        for num in nums:
            if nums[abs(num)-1] < 0: # num show twice
                duplicate.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        
        return duplicate
```

