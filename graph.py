from pprint import pprint


class Graph:
    def __init__(self, g_dict = {}):
        self.graph = g_dict

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for v in self.graph:
            for e in self.graph[v]:
                if {v,e} not in edges:
                    edges.append({v,e})
        return edges

    def add_vertex(self, v):
        self.graph[v] = []

    def add_edge(self, e):
        v1, v2  = e
        if v2 not in self.graph.setdefault(v1, []):
            self.graph[v1].append(v2)
        if v1 not in self.graph.setdefault(v2, []):
            self.graph[v2].append(v1)

#
# a ---- b
# |      |
# |      |
# c ---- d ---- e
#


g_dict ={
    "a": ["b","c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["b", "c", "e"],
    "e": ["d"]
    }

g = Graph(g_dict)
print('vertices: ', g.get_vertices())
print('edges: ', g.get_edges())
print('adding edge af: ', g.add_edge({'a', 'f'}))
print('adding vertex g: ', g.add_vertex('g'))
print('adding vertex eg, bg: ', g.add_edge({'e', 'g'}),
       g.add_edge({'b', 'g'}))

print('vertices: ', g.get_vertices())
print('edges: ', g.get_edges())


def dfs(graph, node, visited=None):
    if not visited:
        visited = []
    visited.append(node)
    for next_v in graph[node]:
        if next_v not in visited:
            dfs(graph, next_v, visited)
    return visited


def dfs_find(graph, node, find, visited=None):
    if not visited:
        visited = []
    if node == find:
        return len(visited)
    if node not in visited:
        visited.append(node)
        for next_v in graph[node]:
            if next_v not in visited:
                res = dfs_find(graph, next_v, find, visited)
                if res:
                    return res
    return None


def bfs(graph, node):
    visited = [node]
    q = [node]
    while q:
        v = q.pop(0)
        for next_v in graph[v]:
            if next_v not in visited:
                q.append(next_v)
                visited.append(next_v)
    return visited


def bfs_find(graph, node, find):
    if find == node:
        return 0
    visited = [node]
    q = [node]
    count = {node:0}
    while q:
        v = q.pop(0)
        for next_v in graph[v]:
            if next_v not in visited:
                q.append(next_v)
                visited.append(next_v)
                count[next_v]= count[v]+1
                if find == next_v:
                    return count[next_v]
    return -1


pprint(g.graph)
print('bfs: ', bfs(g.graph, 'a'))
print('bfs_find e: ', bfs_find(g.graph, 'a', 'e'))
print('bfs_find f: ', bfs_find(g.graph, 'a', 'f'))
print('bfs_find a: ', bfs_find(g.graph, 'a', 'a'))
print('bfs_find k: ', bfs_find(g.graph, 'a', 'k'))

print('dfs: ', dfs(g.graph, 'a'))
print('dfs_find f: ', dfs_find(g.graph, 'a', 'f'))
print('dfs_find e: ', dfs_find(g.graph, 'a', 'e'))
print('dfs_find a: ', dfs_find(g.graph, 'a', 'a'))
print('dfs_find k: ', dfs_find(g.graph, 'a', 'k'))
