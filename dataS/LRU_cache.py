import math
from linked_list import LinkedList

class LRU:
    def __init__( self, N = 10):
        self.M = {}
        self.MAX_SIZE = N
        self.N = 0
        self.L = LinkedList()
    
    def set(self, k, v):
        if k in self.M:
            self.L.remove( self.M[k] )
        else:
            if self.N < self.MAX_SIZE:
                self.N += 1
            else:
                kk = self.L.pop()
                del self.M[kk]
        self.M[k] = self.L.insert(k, v)
    
    def get(self, k):
        if k in self.M:
            v = self.M[k].val

            self.L.remove(self.M[k])
            self.M[k] = self.L.insert(k, v)
            return v
        return -1
    
    def contains(self, k):
        return k in self.M

    def print(self):
        self.L.print()

if __name__ == '__main__':
    lru = LRU(N = 3)
    lru.set(2, 21)
    lru.set(4, 1)
    lru.set(1, 1)
    lru.print()
    lru.set(3, 22)
    lru.print()
    print(lru.get(2))
    lru.print()

    N = 10
    L = math.floor(N*.3)
    B = N-L

    small = LRU(N=L)
    big = LRU(N=B)