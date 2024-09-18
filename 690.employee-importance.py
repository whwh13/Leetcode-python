from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        for k in employees:
            if k.id == id:
                break
        ans += k.importance
        for sub in k.subordinates:
            ans += self.getImportance(employees,sub)
        return ans

employees = [Employee(1,5,[2,3]),Employee(2,3,[]),Employee(3,3,[])]
id = 1 
print(Solution().getImportance(employees, id))