# Design SQL
# https://leetcode.com/problems/design-sql/
# Accepted 2022-09-27 15:38 UTC · Python · 999 ms · 31.3 MB

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {name: {"nextId": 1} for name in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        rowId = self.tables[name]["nextId"]
        self.tables[name][rowId] = row  
        self.tables[name]["nextId"] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        self.tables[name].pop(rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId - 1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)
