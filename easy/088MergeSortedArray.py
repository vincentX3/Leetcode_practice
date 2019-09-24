from typing import List


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, cursor = 0, 0, 0
        while i < m and j < n:
            if nums1[cursor] > nums2[j]:
                nums1.insert(cursor, nums2[j])
                nums1.pop()
                j += 1
            else:
                i += 1
            cursor += 1
        if j < len(nums2):
            for num in nums2[j:]:
                nums1[cursor] = num
                cursor += 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #insert back, quiet similar to merge sort
        m,n,cursor=m-1,n-1,m+n-1
        while m>=0 and n>=0:
            if nums1[m]>=nums2[n]:
                nums1[cursor]=nums1[m]
                m-=1
            else:
                nums1[cursor]=nums2[n]
                n-=1
            cursor-=1
        if n>=0:
            while n>=0:
                nums1[cursor] = nums2[n]
                n -= 1
                cursor -= 1


