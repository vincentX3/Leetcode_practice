class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        length=len(x)-1
        for i in range(int(length/2)+1):
            if x[i]!=x[length-i]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        else:
            half=0
            while half<x:
                half=half*10+x%10
                x//=10

            if half==x or x==half//10:
                return True
            else:
                return False


tests=[3,-121.1221,121,10]
solution=Solution()
for test in tests:
    print(solution.isPalindrome2(test))