class Solution:
    def getSum_failed(self, a: int, b: int) -> int:

        #fail to deal with negative number
        #don't know how to use complement in python
        if a < 0:
            a = ~a  + 1
        if b < 0:
            b = ~b  + 1

        result = a ^ b
        carry = 0
        bit_mask = 1
        flag = False
        while a != 0 and b != 0:
            if flag:
                bit_mask <<= 1  # avoid first round
            flag = True
            a_last, b_last = a & 1, b & 1
            a >>= 1
            b >>= 1
            rectification = (result & bit_mask) ^ carry
            if rectification == 1:
                result |= bit_mask
            elif carry == 1:
                result ^= bit_mask
                pass  # a,b must be 1,0 or 0,1, result should set 0, and carry still be 1
            carry = a_last & b_last

        return result

    def getSum(self, a, b):
        #code from leetcode @pushazhiniao
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


