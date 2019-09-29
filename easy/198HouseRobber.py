class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dynamic programming
        pre,now=0,0
        for future in nums:
            temp=now
            now=max(pre+future,now)
            pre=temp
        return now