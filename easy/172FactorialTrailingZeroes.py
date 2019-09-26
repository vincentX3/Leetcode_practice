class Solution:
    def trailingZeroes1(self, n: int) -> int:
        #result=sum(n//(5^i)) (i<=log5)
        zeroes,base=0,5
        while base<=n:
            zeroes+= n//base
            base*=5
        return zeroes

    def trailingZeroes(self, n: int) -> int:
        #result=sum(n//(5^i)) (i<=log5)
        zeroes=0
        while n>=1:
            zeroes+= n//5
            n//=5
        return zeroes