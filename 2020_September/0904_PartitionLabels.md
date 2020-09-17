# Partition Labels

A string `S` of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

**Example 1:**

```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

 

**Note:**

- `S` will have length in range `[1, 500]`.
- `S` will consist of lowercase English letters (`'a'` to `'z'`) only.

 

  Hide Hint #1 

Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.

## Solution

```
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if len(S) < 1:
            return []
        partition = []
        last = {}
        for idx, letter in enumerate(S):
            last[letter] = idx
        start, i, cur_last = -1, 0, last[S[0]]
        while i < len(S):
            if last[S[i]] > cur_last:
                cur_last = last[S[i]]
            print(i,S[i],cur_last)
            if i == cur_last:
                partition.append(cur_last - start)
                start = i
                cur_last += 1
            i += 1
        return partition
```

