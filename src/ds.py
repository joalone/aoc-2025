class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.count = size

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep != jrep:
            self.parent[irep] = jrep
            self.count -= 1
