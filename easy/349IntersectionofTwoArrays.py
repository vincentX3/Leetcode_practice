from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash={}
        intersection=[]
        for num in nums1:
            hash[num]=num
        for num in nums2:
            if num in hash:
                intersection.append(num)
                hash.pop(num) #去重
        return intersection

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = []

        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            left_val = nums1[left]
            right_val = nums2[right]

            if right_val == left_val:
                intersection.append(nums2[right])
                while right < len(nums2) and nums2[right] == right_val:
                    right += 1
                while left < len(nums1) and nums1[left] == left_val:
                    left += 1
            if right_val > left_val:
                while left < len(nums1) and left_val == nums1[left]:
                    left += 1
            else:
                while right < len(nums2) and right_val == nums2[right]:
                    right += 1
        return intersection