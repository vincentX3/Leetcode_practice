class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits_str(self, n):
        n_str=bin(n)[:1:-1] #convert n to binary representation str, then reverse
        n_str+=(32-len(n_str))*'0'
        return int(n_str,base=2)

    def reverseBits(self, n):
        #divide and conquer
        n_str=bin(n)[2:]
        rev_n=self.reverse(n_str)+(32-len(n_str))*'0'
        return int(rev_n,base=2)

    def reverse(self, sub_str):
        size=len(sub_str)
        if size==1:
            return sub_str
        else:
            return self.reverse(sub_str[size//2:]) +self.reverse(sub_str[:size//2])

    def reverseBits_bit_op(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result
