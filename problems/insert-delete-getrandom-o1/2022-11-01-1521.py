# Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Accepted 2022-11-01 15:21 UTC · Python · 1122 ms · 61.4 MB

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hashmap = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.arr.append(val)
        self.hashmap[val] = self.length
        self.length += 1
        # print('insert', self.arr, self.hashmap)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        idx, last_elem = self.hashmap[val], self.arr[-1]
        self.arr[idx], self.hashmap[last_elem] = last_elem, idx
        self.arr.pop()
        del self.hashmap[val]
        self.length -= 1
        # print('remove', self.arr, self.hashmap)
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
