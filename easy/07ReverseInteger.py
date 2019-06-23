class Solution:
    def reverse(self, x: int) -> int:
        #remember to deal with overflow
        #2^31=2147483648
        if x>=0:
            flag=1
        else:
            flag=-1
            x=-x

        result=x%10
        x=int(x/10)
        while x!=0:
            result=result*10+x%10
            x=int(x/10)
        if flag==-1:
            result=flag*result
        if result>2147483647 or result<-2147483648:
            return 0
        else:
            return result

    #use List method. Consider x as a string
    def reverse2(self,x):
        if x==0:
            return 0
        else:
            x=str(x)
            if '-' in x:
                x=int('-'+''.join(reversed(x[1:])))
            else:
                x=int(''.join(reversed(x)))

            if abs(x)>2**31:
                return 0
            else:
                return x


print(Solution().reverse2(-123))