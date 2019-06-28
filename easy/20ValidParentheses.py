class Solution:
    def isValid(self, s: str) -> bool:
        match={'{':'}','[':']','(':')'}
        stack=[]
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            else:
                try:
                    if char!=match[stack.pop()]:
                        return False
                except IndexError:
                    return False
        if len(stack) == 0:
            return True
        else: return False

    def isValid2(self, s: str) -> bool:
        #more elegant
        match={'{':'}','[':']','(':')'}
        left={"(","[","{"}  #use set
        stack=[]
        for char in s:
            if char in left:
                stack.append(char)
            elif stack and char==match[stack[-1]]:
                stack.pop()
            else:return False

        return stack==[]

tests=['()[]{}','([)]','{[]}',']]]']
solution=Solution()
for test in tests:
    print(solution.isValid2(test))