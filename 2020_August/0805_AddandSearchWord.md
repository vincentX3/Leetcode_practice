# Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

```
void addWord(word)
bool search(word)
```

search(word) can search a literal word or a regular expression string containing only letters `a-z` or `.`. A `.` means it can represent any one letter.

**Example:**

```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

**Note:**
You may assume that all words are consist of lowercase letters `a-z`.



# Solution

```python
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        l = len(word)
        if l not in self.dictionary:
            self.dictionary[l] = set()
        self.dictionary[l].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        l = len(word)
        if l not in self.dictionary:
            return False
        else:
            for ele in self.dictionary[l]:
                if self.match(ele,word):
                    return True
            return False
        
    def match(self, temp: str, aim: str):
        '''
        words have equal length
        '''
        for i in range(len(aim)):
            if aim[i] != '.':
                if aim[i] != temp[i]:
                    return False
        return True
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

