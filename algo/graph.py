from collections import deque
List = list

# BFS in graph
def bfs(self, s, edges: List[List[int]]):
    # edges = adjacency list with weights

    q = deque([s])
    lev = [-1]*self.n
    lev[s] = 0
    while q:
        x = q.popleft()
        for y, w in edges[x]:
            if lev[y] == -1:
                q.append(y)
                lev[y] = lev[x]+1


# DFS in graph
def dfs(self, s, edges: List[List[int]], lev=None):
    # edges = adjacency list with weights

    q = [s]
    lev = [-1]*self.n
    lev[s] = 0
    while q:
        x = q.pop()
        for y, w in edges[x]:
            if lev[y] == -1:
                lev[y] = lev[x] + 1
                q.append(y)



# Graph Algorith to find max flow in network
def ford_fulkerson(source: int, sink: int, graph: List[List[int]]):
    # graph = Matrix with weights

    # preprocessing
    n = len(graph)
    parent = [None]*n

    #function to check if path exist
    def check_path(graph, s, e, n, parent):
        q = deque([s])
        vis = set([s])
        while q:
            x = q.popleft()
            for y in range(n):
                if y not in vis and graph[x][y] > 0:
                    q.append(y)
                    vis.add(y)
                    parent[y] = x
                    if y == e:
                        return True
        return False

    max_flow = 0
    while check_path(graph, source, sink, n, parent):
        pi = parent[sink]
        minW = graph[pi][sink]
        
        while parent[pi] != None:
            minW = min(minW, graph[parent[pi]][pi] )
            pi = parent[pi]

        max_flow += minW

        pi = sink
        while parent[pi] != None:
            graph[parent[pi]][pi] -= minW
            graph[pi][parent[pi]] += minW
            pi = parent[pi]
    return max_flow

import heapq
# finds the single source sortest path to all other vertices
def dijkstra_algo(edges: List[List[int]], n: int, s: int, e:int=None):
    # edges = adjacency list with weights

    dis = [float('inf') for _ in range(self.n)]
    vis = set()
    dis[s] = 0
    pq = [(0, s)]
    while pq:
        disx, x = heapq.heappop(pq)
        if x in vis:
            continue
        vis.add(x)
        for y, wy in edges[x]:
            if y not in vis:
                if dis[y] > disx + wy:
                    dis[y] = disx + wy
                    heapq.heappush(pq, (dis[y], y))
    if e == None:
        return dis
    return dis[e]

# printing edges of ST
def print_edges(result):
    for u, v, weight in result:
        print("%d - %d: %d" % (u, v, weight))

# finds minimum Weighted Segment Tree
def prims_algo(edges: List[List[int]], n: int):
    # edges = adjacency list with weights

    vis = set()
    stedges = []
    pq = [(0, 0, 0)]
    while pq:
        wx, x, px = heapq.heappop(pq)
        if x in vis:
            continue
        vis.add(x)
        stedges.append((px, x, wx))
        for y, wy in edges[x]:
            if y not in vis:
                heapq.heappush(pq, (wy, y, x))
    
    return stedges[1:]
    
    # return minimum weight of Segment Tree
    # return sum( x[2] for x in stedges)
    # print_edges(stedges)

print(prims_algo([ [ [1, 3], [2,5], [5, 2] ], [ [0, 2], [2,8], [4, 5] ], [ [1, 3], [5,5] ], [ [1, 3], [2,5], [0, 2] ], [ [3,2], [1, 8] ], [ [1, 3], [2,5], [3, 2], [0, 2]]] , 6))
import union_find as UF

# Kruskal algorithm //   gives a shortest segment tree
def kruskal_algo(edges: List[List[int]], N: int):
    # edges => list of edges in form (x, y, w)
    # N = number of Vertices
    '''
    we first sort all edges and then try to add each edge into spanning tree
    and we check if adding an edge form a cycle then we skip that edge
    So, sorting Edges takes => E.log(E)
    and also, we use union find method to find cycle it also takes => E.log(E)
    '''

    result = []
    i, e = 0, 0
    graph = sorted(edges, key=lambda item: item[2])
    unionFind = UF.UnionFind(N)
    while e < N - 1:
        u, v, w = graph[i]
        i = i + 1
        if not unionFind.find(u, v):
            e = e + 1
            result.append([u, v, w])
            unionFind.union(u, v)

    return result
    # Printing the Edges of ST
    # print_edges(result)

print(kruskal_algo( [ [0, 1, 3], [0, 2, 5], [0, 5, 2], [1, 0, 2], [1, 2, 8], [1, 4, 5], [2, 1, 3], [2, 5, 5], [3, 1, 3], [3, 2, 5], [3, 0, 2], [4, 3, 2], [4, 1, 8], [5, 1, 3], [5, 2, 5], [5, 3, 2], [5, 0, 2] ], 6) )
# finds the all pair sortest paths and checks negative cycle
def bellman_ford(src: int, n: int, edges: List[List[int]]):
    # Edges = List of (v1, v2, w)

    dist = [float("Inf")] * n
    dist[src] = 0

    for _ in range(n - 1):
        for s, d, w in edges:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                dist[d] = dist[s] + w

    for s, d, w in edges:
        if dist[s] != float("Inf") and dist[s] + w < dist[d]:
            # print("Graph contains negative weight cycle")
            return False
    
    return True