
class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = list(range(N))
        self.rank = [1]*N

    def find_parent(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.parent[self.parent[i]]
        return self.find_parent(self.parent[i])

    def find(self, x, y): return self.find_parent(x) == self.find_parent(y)

    def union(self, x, y):
        xroot = self.find_parent(x)
        yroot = self.find_parent(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
