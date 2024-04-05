from queue import PriorityQueue

dict_hn = {
    "Arad": 336, "Bucharest": 0, "Craiova": 160, "Drobeta": 242,
    "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
    "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesti": 100, "Rimnicu": 193, "Sibiu": 253,
    "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
}

dict_gn = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Bucharest": {"Urziceni": 85, "Giurgiu": 90, "Pitesti": 101, "Fagaras": 211}
}

start = "Arad"
goal = "Bucharest"
result = ""

class Node:
    def __init__(self, total, city_str):
        self.total = total
        self.city_str = city_str

    def get_total(self):
        return self.total

    def get_city_str(self):
        return self.city_str

def get_fn(city_str):
    cities = city_str.split(" , ")
    gn = sum(dict_gn[cities[i]][cities[i + 1]] for i in range(len(cities) - 1))
    hn = dict_hn[cities[-1]]
    return hn + gn

def expand(city_str, city_queue):
    this_city = city_str.split(" , ")[-1]
    if this_city == goal:
        global result
        result = city_str
        return
    if this_city not in dict_gn:
        return  # No neighbors defined for this city
    print("Expanding city:", this_city, ", Total cost:", get_fn(city_str))
    for city, cost in dict_gn[this_city].items():
        city_queue.put((get_fn(city_str + " , " + city), city_str + " , " + city))
    if not city_queue.empty():
        expand(city_queue.get()[1], city_queue)

city_queue = PriorityQueue()
expand(start, city_queue)
print("The A* path with the total is:", result)
