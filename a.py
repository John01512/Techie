import queue as Q

# Heuristic values for each city, representing the estimated cost from the current city to the goal city
dict_hn = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
           'Eforie': 161, 'Fagaras': 178, 'Giurgiu': 77, 'Hirsova': 151,
           'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
           'Oradea': 380, 'Pitesti': 98, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
           'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

# Path costs from each city to its neighbors
dict_gn = {'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
           'Bucharest': {'Urziceni': 85, 'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211},
           'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
           'Drobeta': {'Mehadia': 75, 'Craiova': 120},
           'Eforie': {'Hirsova': 86},
           'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
           'Giurgiu': {'Bucharest': 90},
           'Hirsova': {'Eforie': 86, 'Urziceni': 98},
           'Iasi': {'Neamt': 87, 'Vaslui': 92},
           'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
           'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
           'Neamt': {'Iasi': 87},
           'Oradea': {'Zerind': 71, 'Sibiu': 151},
           'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101, 'Craiova': 138},
           'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
           'Sibiu': {'Rimnicu Vilcea': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
           'Timisoara': {'Lugoj': 111, 'Arad': 118},
           'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
           'Vaslui': {'Iasi': 92, 'Urziceni': 142},
           'Zerind': {'Oradea': 71, 'Arad': 75}}

# Starting city and goal city for the A* search
start = 'Arad'
goal = 'Bucharest'

result = ''  # Variable to store the final result

# Function to calculate the total cost (fn) for a given path
def get_fn(citystr):
    cities = citystr.split(",")
    hn = gn = 0  # Initialize heuristic and path costs
    for ctr in range(0, len(cities) - 1):
        gn = gn + dict_gn[cities[ctr]][cities[ctr + 1]]  # Calculate path cost
    hn = dict_hn[cities[len(cities) - 1]]  # Get heuristic cost
    return (hn + gn)  # Return the sum of path cost and heuristic cost

# Function to expand the search by exploring neighboring cities
def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get()  # Get the next city to explore from the priority queue
    if thiscity == goal:
        result = citystr + "::" + str(tot)  # If the goal city is reached, update the result
        return
    for cty in dict_gn[thiscity]:  # Iterate over neighboring cities
        cityq.put((get_fn(citystr + "," + cty), citystr + "," + cty, cty))  # Add neighboring cities to the priority queue
    expand(cityq)  # Recursively expand the search

# Main function to initiate the A* search
def main():
    cityq = Q.PriorityQueue()  # Initialize a priority queue to store cities to explore
    thiscity = start  # Start the search from the starting city
    cityq.put((get_fn(start), start, thiscity))  # Add the starting city to the priority queue
    expand(cityq)  # Expand the search
    print("The A* path with the total is: ")
    print(result)  # Print the final result

main()  # Call the main function to start the A* search