import queue as Q  # Importing the queue module for priority queue implementation

# Heuristic values for each city estimating the cost to reach the goal city (Bucharest)
dict_hn = {'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
           'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
           'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
           'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

# Actual costs of traveling between cities
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

start = 'Arad'  # Starting city
goal = 'Bucharest'  # Goal city
result = ''  # Variable to store the result path

def get_fn(citystr):
    """
    Calculate the total cost (f(n)) for a given path represented by the string citystr.

    Args:
    citystr (str): A string representing the path of cities.

    Returns:
    int: The total cost of the path.
    """
    cities = citystr.split(',')
    hn = gn = 0
    for ctr in range(0, len(cities)-1):
        gn = gn + dict_gn[cities[ctr]][cities[ctr+1]]
    hn = dict_hn[cities[len(cities)-1]]
    return hn + gn

def printout(cityq):
    """
    Print the contents of the priority queue cityq.

    Args:
    cityq (queue.PriorityQueue): Priority queue containing cities.
    """
    for i in range(0, cityq.qsize()):
        print(cityq.queue[i])

def expand(cityq):
    """
    Expand the current city by adding its neighbors to the priority queue based on their f(n) values.

    Args:
    cityq (queue.PriorityQueue): Priority queue containing cities.
    """
    global result
    tot, citystr, thiscity = cityq.get()
    nexttot = 999
    if not cityq.empty():
        nexttot, nextcitystr, nextthiscity = cityq.queue[0]
    if thiscity == goal and tot < nexttot:
        result = citystr + '::' + str(tot)
        return
    print("Expanded city------------------------------", thiscity)
    print("Second best f(n)------------------------------", nexttot)
    tempq = Q.PriorityQueue()
    for cty in dict_gn[thiscity]:
        tempq.put((get_fn(citystr + ',' + cty), citystr + ',' + cty, cty))
    for ctr in range(1, 3):
        ctrtot, ctrcitystr, ctrthiscity = tempq.get()
        if ctrtot < nexttot:
            cityq.put((ctrtot, ctrcitystr, ctrthiscity))
        else:
            cityq.put((ctrtot, citystr, thiscity))
            break
    printout(cityq)
    expand(cityq)

def main():
    
    cityq = Q.PriorityQueue()
    thiscity = start
    cityq.put((999, "NA", "NA"))
    cityq.put((get_fn(start), start, thiscity))
    expand(cityq)
    print(result)

main()