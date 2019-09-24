class Solution:
    def romanToInt(self, s: str) -> int:
        map={'I':1,'V':5,'IV':4,'X':10,'IX':9,
             'L':50,'XL':40,'C':100,'XC':90,
             'D':500,'CD':400,'M':1000,'CM':900}
        sum=0
        last=len(s)-1
        index=0
        while index<last:
            val=map.get(s[index]+s[index+1])
            if val==None:
                sum+=map.get(s[index])
                index+=1
            else:
                sum+=val
                index+=2
        if index==last:
            sum+=map.get(s[index])

        return sum


    def romanToInt2(self, s: str) -> int:
        #so pythonic
        map={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        sum,pre=0,'I'
        for cur in s[::-1]:
            sum,pre=sum+map[cur] if map[cur]>=map[pre] else sum-map[cur], cur
        return sum


    def romanToInt3(self, s: str) -> int:
        #damn it, so brute.
        m = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(m.get, s))

tests=["III",'IX','XI','LVIII','MCMXCIV']
solution=Solution()
for test in tests:
    print(solution.romanToInt3(test))