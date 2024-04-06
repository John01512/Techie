class RomanianMap:
    def __init__(self):
        # Define the map of Romania as a dictionary where each city is a key
        # and the value is a list of neighboring cities
        self.romania_map = {
            'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
            'Zerind': ['Arad', 'Oradea'],
            'Oradea': ['Zerind', 'Sibiu'],
            'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
            'Timisoara': ['Arad', 'Lugoj'],
            'Lugoj': ['Timisoara', 'Mehadia'],
            'Mehadia': ['Lugoj', 'Drobeta'],
            'Drobeta': ['Mehadia', 'Craiova'],
            'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
            'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
            'Fagaras': ['Sibiu', 'Bucharest'],
            'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
            'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
            'Giurgiu': ['Bucharest'],
            'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
            'Hirsova': ['Urziceni', 'Eforie'],
            'Eforie': ['Hirsova'],
            'Vaslui': ['Urziceni', 'Iasi'],
            'Iasi': ['Vaslui', 'Neamt'],
            'Neamt': ['Iasi']
        }

    def DLS(self, city, visitedstack, startlimit, endlimit, goal):
        global result
        found = 0
        result = result + city + ' '  # Append current city to the result path
        visitedstack.append(city)
        if city == goal:
            return 1  # Goal city found, return success
        if startlimit == endlimit:
            return 0  # Depth limit reached, return failure
        for eachcity in self.romania_map[city]:
            if eachcity not in visitedstack:
                found = self.DLS(eachcity, visitedstack, startlimit + 1, endlimit, goal)
                if found:
                    return found  # Goal found in child, return success

    def IDDFS(self, city, visitedstack, endlimit, goal):
        global result
        for i in range(0, endlimit):
            print("Searching at Limit:", i)
            found = self.DLS(city, visitedstack, 0, i, goal)
            if found:
                print("Found")
                break  # Goal found, exit loop
            else:
                print("Not Found!")
                print(result)  # Print current path
                print(" ---- ")
                result = ''  # Reset result for next iteration
                visitedstack = []  # Clear visited stack for next iteration

map_instance = RomanianMap()
start = 'Arad'
goal = 'Bucharest'
result = ''
visitedstack = []
map_instance.IDDFS(start, visitedstack, 10, goal)
print("IDDFS Traversal from", start, "to", goal, "is:")
print(result)