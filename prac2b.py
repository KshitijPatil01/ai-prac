
# DFS using Graph

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()

def dfs(node, goal):

    if node == goal:
        print("Goal Found:", node)
        return True

    visited.add(node)
    print("Visiting:", node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs(neighbour, goal):
                return True

    return False


start = 'A'
goal = 'F'

print("DFS Traversal:")

if not dfs(start, goal):
    print("Goal not found")
