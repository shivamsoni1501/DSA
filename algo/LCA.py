

pp = []
l = []

def LCA_Preprocessing(N, edges: List[List[int]]):
    # edges = adjacency list of edges
    global pp, l

    # parent
    p = [None]*N
    l = [0]*N

    # max bits in N
    MAX2 = 20

    def dfs(s, p, l):
        stack = [s]
        p[s] = s
        l[s] = 0
        while stack:
            x = stack.pop()
            for y in Tree[x]:
                if p[y]==None:
                    p[y] = x
                    l[y] = l[x]+1
                    stack.append(y) 

    dfs(0, p, l)
    # parent of parents
    pp = [ [None]*MAX2 for _ in range(N) ]
    for i in range(N):
        pp[i][0] = p[i]
    for j in range(1, MAX2):
        for i in range(N):
            pp[i][j] = pp[pp[i][j-1]][j-1]

def LCA_Q(x: int, y: int):
    if l[x]>l[y]:
        x, y = y, x
    d = l[y]-l[x]
    if d!=0:
        for i in range(MAX2-1,-1, -1):
            if d&(1<<i):
                d -= 1<<i
                y = pp[y][i]
    if x == y:
        return x+1
    for i in range(MAX2-1, -1, -1):
        if pp[x][i] != pp[y][i]:
            x = pp[x][i]
            y = pp[y][i]
    return pp[x][0]+1


# def searchLCA(x, y):
#     if l[x]>l[y]:
#         x, y = y, x
#     d = l[y]-l[x]
#     if d!=0:
#         for i in range(MAX2-1,-1, -1):
#             if d>=1<<i:
#                 d -= 1<<i
#                 y = pp[y][i]
#     if x == y:
#         return x+1
#     for i in range(MAX2-1, -1, -1):
#         if pp[x][i] != pp[y][i]:
#             x = pp[x][i]
#             y = pp[y][i]
#     return pp[x][0]+1

# N = int(input())
# Tree = [ [] for _ in range(N) ]
# MAX2 = 20
# for _ in range(N-1):
#     x, y = map(int, input().split())
#     x -= 1
#     y -= 1
#     Tree[x].append(y)
#     Tree[y].append(x)

# p = [None]*N
# l = [0]*N
# dfs(0, p, l)

# # parent of parents list
# pp = [ [None]*MAX2 for _ in range(N) ]

# for i in range(N):
#     pp[i][0] = p[i]

# for j in range(1, MAX2):
#     for i in range(N):
#         pp[i][j] = pp[pp[i][j-1]][j-1]
# # print(pp)

# Q = int(input())
# for _ in range(Q):
#     r, x, y = map(int, input().split())
#     r -= 1
#     x -= 1
#     y -= 1
#     rr = searchLCA(x, y)
#     xx = searchLCA(r, y)
#     yy = searchLCA(x, r)
#     print(rr, xx, yy)
#     if xx == yy:
#         print(rr)
#     elif xx == rr:
#         print(yy)
#     else:
#         print(xx)