from collections import deque

# Topological sorting dfs
def recurse(i, arr, A, V):
    V[i] = True
    for j in range(N):
        if arr[i][j] == 1 and not V[j]:
            recurse(j, arr, A, V)
    A.append(i)

def topological_sort(arr):
    N = len(arr)
    A = []
    V = [False]*N
    for i in range(N):
        if not V[i]:
            recurse(i, arr, A, V)
    return A[::-1]

# Topological soting BFS
def topological_sort_bfs(arr):
    N = len(arr)
    in_edges = [0]*N
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                in_edges[j] += 1
    
    q = deque([])
    for i in range(N):
        if in_edges[i] == 0:
            q.append(i)
    l = []

    while q:
        i = q.popleft()
        l.append(i)
        for j in range(N):
            if arr[i][j] == 1 and in_edges[j] != 0:
                in_edges[j] -= 1
                if in_edges[j] == 0:
                    q.append(j)
    return l