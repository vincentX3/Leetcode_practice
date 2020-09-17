# Design HashSet

Solution

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

- `add(value)`: Insert a value into the HashSet. 
- `contains(value)` : Return whether the value exists in the HashSet or not.
- `remove(value)`: Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.


**Example:**

```
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)
```


**Note:**

- All values will be in the range of `[0, 1000000]`.
- The number of operations will be in the range of `[1, 10000]`.
- Please do not use the built-in HashSet library.

# Solution

my simple solution:

> Since all inserted elements are number, we could easily use `%` as a hash function. The only work we have to do is **decide a suitable mod number.**

```python
class MyHashSet:
    _size = 10000

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [[] for _ in range(MyHashSet._size)]
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset[key%MyHashSet._size].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset[key%MyHashSet._size].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hashset[key%MyHashSet._size]:
            return True
        else: 
            return False
```



Brilliant tricks below (copy from Leetcode leader board):

> Since description already gives the range of value, we could just use a byte array to maintain each number's condition.

```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = bytearray(1000001)

        
    def add(self, key: int) -> None:
        
        if not self.hash_set[key]:
		
			# set to True for existence of incoming element
            self.hash_set[key] = True

            
    def remove(self, key: int) -> None:
        
        if self.hash_set[key]:
		
			# clear to False for removal
            self.hash_set[key] = False

            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
		# check the flag for existence judgement
        if self.hash_set[key]:
            return True
			
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

