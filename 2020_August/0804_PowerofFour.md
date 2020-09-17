# Power of Four

Solution

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

**Example 1:**

```
Input: 16
Output: true
```

**Example 2:**

```
Input: 5
Output: false
```

**Follow up**: Could you solve it without loops/recursion?



# Solution

1. Using loops

   ```python
   class Solution:
       def isPowerOfFour(self, num: int) -> bool:
           if num<=0:
               return False
           while num>1:
               if num%4 != 0:
                   return False
               else:
                   num >>= 2
           return True
       
       
   # more elegant way
   class Solution:
       def isPowerOfFour(self, n: int) -> bool:
           if n < 1:
               return False
           while n%4 == 0:
               n /= 4
           return True if n==1 else False
   ```

   

2. Convert it to binary.

	```python
	class Solution:
	    def isPowerOfFour(self, num: int) -> bool:
	        if num<=0:
	            return False
	        n_bin=bin(num)[2:]
	        return n_bin.count('0')%2==0 and n_bin.count('1')==1
	```

