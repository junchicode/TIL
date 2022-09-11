graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[5,6],
    6:[],
    7:[3]
}

def dfs_rec(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if not w in visited:
            visited = dfs_rec(w, visited)
    return visited

print(dfs_rec(1, visited=[]))