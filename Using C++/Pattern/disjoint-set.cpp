class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        # Optional: size array
        self.size = [1] * n

    # Path Compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by Rank
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]

        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]

        else:
            self.parent[py] = px
            self.rank[px] += 1
            self.size[px] += self.size[py]

        return True
