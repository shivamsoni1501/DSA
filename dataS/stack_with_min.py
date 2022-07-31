
#with O(1) space
class Stack:

    def __init__(self):
        self.stack = []
        self.minE = float('inf')

    def getM(self):
        return self.minE

    def push(self, val):
        if val < self.minE:
            newV = 2*val-self.minE
            self.minE = val
            self.stack.append(newV)
        else:
            self.stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val < self.minE:
            oVal = self.minE
            self.minE = 2*oVal - val
            return oVal
        return val
