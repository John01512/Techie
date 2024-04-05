from collections import deque

romania_map = {
    "Arad": ["Sibiu", "Zerind", "Timisoara"],
    "Zerind": ["Arad", "Oradea"],
    "Oradea": ["Zerind", "Sibiu"],
    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],
    "Craiova": ["Drobeta", "Rimnicu", "Pitesti"],
    "Rimnicu": ["Sibiu", "Craiova", "Pitesti"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Pitesti": ["Rimnicu", "Craiova", "Bucharest"],
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucharest"],
    "Urziceni": ["Bucharest", "Vaslui", "Hirsova"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],
    "Vaslui": ["Iasi", "Urziceni"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"]
}

def bfs(starting_node, destination_node):
    visited = {city: False for city in romania_map}
    parent = {city: None for city in romania_map}
    queue = deque()
    bfs_traversal_output = []
    
    starting_city = starting_node
    visited[starting_city] = True
    queue.append(starting_city)
    
    while queue:
        u = queue.popleft()
        bfs_traversal_output.append(u)
        print("Expanding node:", u)
        for v in romania_map[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    
    path = []
    g = destination_node
    while g:
        path.append(g)
        g = parent[g]
    
    path.reverse()
    print("Shortest path:", path)

bfs("Arad", "Bucharest")
