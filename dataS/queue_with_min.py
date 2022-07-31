from collections import deque

class MinQueue:
    def __init__(self):
        self.q = deque([])
        self.curI = 0
    

    def push(self, val, i):
        while len(self.q)!=0 and self.q[-1][0] >= val:
            self.q.pop()
        self.q.append((val, i))

    def pop(self):
        if self.curI >= self.q[0][1]:
            self.q.popleft()
        self.curI += 1
    
    def min(self):
        return self.q[0][0] if len(self.q)!=0 else -float('inf')
        
q = MinQueue()

arr = [10, 2,4,12,12,123,41,24,1,24,1]

for i in range(9):
    q.push(arr[i], i)

q.pop()
print(q.min())

q.pop()
q.pop()
q.pop()
print(q.min())


q.pop()
print(q.min())
