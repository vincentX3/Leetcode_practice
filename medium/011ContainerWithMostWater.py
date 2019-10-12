from typing import List


class Solution:
    def maxArea_BF(self, height: List[int]) -> int:
        #brute-force O(n^2) Time limited exceeded
        max_area = 0
        for left, h in enumerate(height):
            for right in range(left + 1, len(height)):
                distance = right - left
                real_h = min(h, height[right])
                area = distance * real_h
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        max_area=(right-left)*min(height[left],height[right])
        while left<right:
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            area=(right-left)*min(height[left],height[right])
            if area>max_area:
                max_area=area

        return max_area