class Solution_recur:
    def __init__(self):
        self.record={}
        self.max_palindrome=''
    def longestPalindrome(self, s: str) -> str:
        # print(self.max_palindrome)
        length=len(s)
        if length < 2 or self.testPalindrome(s):
            if len(s) > len(self.max_palindrome):
                self.max_palindrome = s
            self.record[s] = s
            return s

        else:
            if length-1 <= len(self.max_palindrome):
                return self.max_palindrome
            else:
                left=self.record.setdefault(s[:-1],self.longestPalindrome(s[:-1]))
                right=self.record.setdefault(s[1:],self.longestPalindrome(s[1:]))
                return max(left, right,key=lambda x:len(x))

    def testPalindrome(self, s: str):
        # check whether str is palindrome
        return s == s[::-1]

class Solution_dummy:
    def __init__(self):
        self.max_palindrome=''
        self.queue=[]
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 :
            return s
        self.queue.append(s)
        while len(self.queue)>0:
            s=self.queue.pop(0)
            if len(s) < 2 or self.testPalindrome(s):
                if len(s) > len(self.max_palindrome):
                    self.max_palindrome = s
            else:
                if len(s) - 1 <= len(self.max_palindrome):
                    pass
                else:
                    self.queue.append(s[:-1])
                    self.queue.append(s[1:])
        return self.max_palindrome


    def testPalindrome(self, s: str):
        # check whether str is palindrome
        return s == s[::-1]


class Solution_dp:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        #initialize dp container
        dp=[[False]*length for _ in range(length)]
        #global optimum's index
        ans_left,ans_right=0,0

        for i in range(length):
            left,right=length-1-i,length-1-i
            while right<length:
                #check base situation
                if left==right:
                    dp[left][right]=True
                elif right-left==1 and s[left]==s[right]:
                    #e.g. "aa"
                    dp[left][right]=True

                #common requirements
                elif dp[left+1][right-1] and s[left]==s[right]:
                    dp[left][right]=True

                if dp[left][right] and (right-left)>(ans_right-ans_left):
                    ans_left,ans_right=left,right

                #update index
                right+=1
        return s[ans_left:ans_right+1]


class Solution_expand:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        # global optimum's index
        ans=''
        for i in range(length-1):
            odd=self.expand_check(s,i,i)
            even=self.expand_check(s,i,i+1)
            ans=max(ans,odd,even,key=lambda x:len(x))
        return ans

    def expand_check(self,s,left,right):
        while s[left]==s[right]:
            left-=1
            right+=1
            if left<0 or right>=len(s):
                break
        return s[left+1:right]


s=Solution_expand()
tests=["babad","","cbbd","abcdcb","babaddtattarrattatddetartrateedredividerb"]
for test in tests:
    print(s.longestPalindrome(test))