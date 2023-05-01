# Snapshot Array
# https://leetcode.com/problems/snapshot-array/
# Accepted 2023-05-01 02:00 UTC · Python · 701 ms · 41.8 MB

class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[(0, -1)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        prev_val, prev_snapid = self.data[index][-1]
        if prev_val != val:
            if prev_snapid == self.snap_id:
                self.data[index].pop()
            self.data[index].append((val, self.snap_id))
            
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pos = bisect_right(self.data[index], snap_id, key=lambda x: x[1])
        while pos == len(self.data[index]) or self.data[index][pos][1] > snap_id:
            pos -= 1
        return self.data[index][pos][0]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
