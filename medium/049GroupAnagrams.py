from typing import List


class Solution:
    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            temp = sorted(str)
            temp = ''.join(temp)
            if temp in anagrams:
                anagrams[temp].append(str)
            else:
                anagrams[temp] = [str]
        return [val for val in anagrams.values()]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash by counter
        anagrams = {}
        for string in strs:
            counter = [0 for _ in range(26)]  # only lower case
            for letter in string:
                counter[ord(letter) - ord('a')] += 1
            temp = str(counter)
            if temp in anagrams:
                anagrams[temp].append(string)
            else:
                anagrams[temp] = [string]
        return [val for val in anagrams.values()]
