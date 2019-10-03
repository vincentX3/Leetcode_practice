class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        n_bin = bin(num)[2:]
        return n_bin.count('0') % 2 == 0 and n_bin.count('1') == 1

    def isPowerOfFour_loop(self, num: int) -> bool:
        if num<=0:
            return False
        while num&3==0:
            num>>=2
        return num==1