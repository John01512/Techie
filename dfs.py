class Two:
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

    goal = "Bucharest"

    @staticmethod
    def dls(city, visited_stack, start_limit, end_limit):
        if city not in Two.dict_gn:
            print("City", city, "has no neighbors defined.")
            return 0
        if start_limit == end_limit:
            return 0
        if city == Two.goal:
            print("Reached goal city:", city)
            return 1
        visited_stack.append(city)
        for each_city in Two.dict_gn[city]:
            if each_city not in visited_stack:
                found = Two.dls(each_city, visited_stack, start_limit + 1, end_limit)
                if found == 1:
                    return 1
        return 0

    @staticmethod
    def iddfs(city, visited_stack, end_limit):
        result = ""
        for i in range(end_limit):
            found = Two.dls(city, visited_stack, 0, i)
            if found == 1:
                print("Found")
                break
            else:
                print("Not Found! ")
                result = ""
                visited_stack.clear()


start = "Arad"
result = ""
visited_stack = []
Two.iddfs(start, visited_stack, 9)
print("IDDFS Traversal from", start, "to", Two.goal, "is:")
print(result)
