# 232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.

- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

Example:

MyQueue queue = new MyQueue();

> queue.push(1);  
queue.push(2);    
queue.peek();  // returns 1  
queue.pop();   // returns 1  
queue.empty(); // returns false

Notes:

- You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
- You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
---
## Solutions:
先吐槽下，在`leetcode`的评测系统，同样的代码提交两次，运行效率差异有点惊人←。←  
（在这道大家水平差矩不大的题目上，同样的代码实现了17.8%→98.3%的飞跃😂

1. python原生`list`操作  
都知道python的`list`本来就实现了队列和栈的全部操作，重新封装了下罢。
2. 辅助栈来倒序
老老实实做题😂
使用一个辅助栈，出队队首元素时，用`stack.pop()`将栈中其他元素转移到辅助栈。
> 实际使用，根据操作场景决定辅助栈是用来帮助入队还是出队。（既我们的“队列”的队首是在栈顶还是栈尾）

