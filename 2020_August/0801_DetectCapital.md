# Detect Capital



Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

 

**Example 1:**

```
Input: "USA"
Output: True
```

 

**Example 2:**

```
Input: "FlaG"
Output: False
```

 

**Note:** The input will be a non-empty word consisting of uppercase and lowercase latin letters.



# Solution

First day challenge, quite easy one. We could use a finite state machine to describe the letter's rule.

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == "":
            return False
        if len(word) == 1:
            return True
        else:
            if word[0].islower():
                return word[1:].islower()
            else:
                # first letter is capital
                # remaining letters should all be capital or not.
                if word[1:].islower() or word[1:].isupper():
                    return True
                else:
                    return False
```

