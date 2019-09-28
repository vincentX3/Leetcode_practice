class Solution(object):
    def hammingWeight_simple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n>0:
            count+=n&1
            n>>=1
        return  count