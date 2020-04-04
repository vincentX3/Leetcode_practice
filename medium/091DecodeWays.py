class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        dynamic programming. the zero had to be carefully handled.
        '''
        if not s:
            return 0
        length = len(s)
        dp = [1 for _ in range(length)]

        # init base situation
        if s[0] == '0' and not self.check_valid_zero(s, 0):
            return 0
        if length > 1:
            if s[1] != '0' and self.check_word(s, 1):
                dp[1] = 2
            elif s[1] == '0' and not self.check_valid_zero(s, 1):
                return 0

        # dp
        for i in range(2, length):
            if s[i] != '0':
                if self.check_word(s, i):
                    dp[i] = dp[i - 2] + dp[i - 1]
                else:
                    dp[i] = dp[i - 1]
            else:
                if not self.check_valid_zero(s, i):
                    return 0
                else:
                    dp[i] = dp[i - 2]
        return dp[-1]

    def check_valid_zero(self, s, idx):
        '''
        input:s[idx]=='0'
        return True if the zero can be decoded.
        '''
        if idx == 0:
            return False
        # check previous digit
        return self.check_word(s, idx)

    def check_word(self, s, idx):
        if s[idx - 1] == '0':
            return False
        return int(s[idx - 1:idx + 1]) > 0 and int(s[idx - 1:idx + 1]) <= 26

    def numDecodings_leetcode(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1:i]):  # (2)
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]

        return dp[-1]
