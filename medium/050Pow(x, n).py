class Solution:
    def myPow1(self, x: float, n: int) -> float:
        # dummy but simplest version
        return x ** n

    def myPow2(self, x: float, n: int) -> float:
        # dummy recursive Time Limit Exceeded
        flag = True if n < 0 else False
        n = abs(n)
        if n == 0:
            return 1
        ans = self.myPow2(x, n // 2) * self.myPow2(x, n // 2) * x if n & 1 else (
                self.myPow2(x, n // 2) * self.myPow2(x, n // 2))
        return 1 / ans if flag else ans

    def myPow3(self, x: float, n: int) -> float:
        # dummy dynamic programming Memory Limit Exceeded
        flag = True if n < 0 else False
        n = abs(n)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i // 2] * dp[i // 2]
            if i & 1:  # odd
                dp[i] *= x
        return 1 / dp[-1] if flag else dp[-1]

    def myPow(self, x: float, n: int) -> float:
        dp = []
        flag = True if n < 0 else False
        n = abs(n)
        while n > 0:
            if n & 1:
                dp.append(1)
            else:
                dp.append(0)
            n >>= 1
        dp.append(1)  # dp[-1]=1, just the same meaning as dp[0]=1
        print(dp)
        for i in range(2, len(dp) + 1):
            if dp[-i]:
                dp[-i] = dp[-i + 1] * dp[-i + 1] * x
            else:
                dp[-i] = dp[-i + 1] * dp[-i + 1]
        return 1 / dp[0] if flag else dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(4, -3))
