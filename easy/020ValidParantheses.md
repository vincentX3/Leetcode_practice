### 20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

> Input: "()"
Output: true

Example 2:

> Input: "()[]{}"
Output: true

Example 3:

> Input: "(]"
Output: false

Example 4:

> Input: "([)]"
Output: false

Example 5:

> Input: "{[]}"
Output: true

---
solution:
维护一个**栈**可以很轻松的解决本题。
对于python而言，使用`dict` 和 `set` 使代码简洁。