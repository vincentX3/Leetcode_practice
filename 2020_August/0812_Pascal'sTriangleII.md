# Pascal's Triangle II

Given a non-negative index *k* where *k* ≤ 33, return the *k*th index row of the Pascal's triangle.

Note that the row index starts from 0.

![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Example:**

```
Input: 3
Output: [1,3,3,1]
```

**Follow up:**

Could you optimize your algorithm to use only *O*(*k*) extra space?



# Solution

Take it as a **dynamic programming** problem, whose formula could easily be describe by $DP[i]=DP[i-1]+DP[i]$.

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        array = [ 0 for _ in range(rowIndex+1)]
        array[0] = 1
        for row in range(1,rowIndex+1):
            temp = 1
            for i in range(1,row+1):
                array[i],temp = array[i] + temp, array[i]
            print(array)    
        return array
```

