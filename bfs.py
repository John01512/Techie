from collections import deque

def bfs(visited, graph, node):
    visited.append(node)
    queue = deque([node])
    while queue:
        m = queue.popleft()
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": []
}

visited = []
print("Following is the Breadth First Search: ")
bfs(visited, graph, "7")
