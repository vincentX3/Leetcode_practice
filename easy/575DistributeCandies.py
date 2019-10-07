from typing import List
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candies_set = set(candies)
        return min(len(candies_set),len(candies)//2)

    def distributeCandies2(self, candies: List[int]) -> int:
        candies_hash={candy:candy for candy in candies}
        return min(len(candies_hash),len(candies)//2)

    def distributeCandies3(self, candies: List[int]) -> int:
        candies.sort()
        count=1
        max_count=len(candies)//2
        if max_count==0:
            return 0
        pre=candies[0]
        for candy in candies[1:]:
            if candy!=pre:
                count+=1
            if count>=max_count:
                count=max_count
                break
            pre=candy
        return count