# H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): "A scientist has index *h* if *h* of his/her *N* papers have **at least** *h* citations each, and the other *N − h* papers have **no more than** *h* citations each."

**Example:**

```
Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
```

**Note:** If there are several possible values for *h*, the maximum one is taken as the h-index.



# Solution

1. First `sort()`, remember the question said that  *h* means papers have **at least** *h* citations each while remaining *N-h* have **no more than** *h*, which can be translated into code.  

   ```python
   class Solution:
       def hIndex(self, citations: List[int]) -> int:
           if len(citations) < 1:
               return 0
           citations.sort()
           h, N = 0, len(citations)
           
           for i in range(1,min(citations[-1]+1,N+1)):
               print(i,citations[-i])
               if i <= citations[-i]:
                   h = i
               else: break
           return h
   ```