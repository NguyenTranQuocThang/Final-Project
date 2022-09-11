
import math
import heapq


class M:
    def __init__(self):
        self.intersections = {0: [0.7798606835438107, 0.6922727646627362],
                              1: [0.7647837074641568, 0.3252670836724646],
                              2: [0.7155217893995438, 0.20026498027300055],
                              3: [0.7076566826610747, 0.3278339270610988],
                              4: [0.8325506249953353, 0.02310946309985762],
                              5: [0.49016747075266875, 0.5464878695400415],
                              6: [0.8820353070895344, 0.6791919587749445],
                              7: [0.46247219371675075, 0.6258061621642713],
                              8: [0.11622158839385677, 0.11236327488812581],
                              9: [0.1285377678230034, 0.3285840695698353]}
        self.roads = [[7, 6, 5],
                      [4, 3, 2],
                      [4, 3, 1],
                      [5, 4, 1, 2],
                      [1, 2, 3],
                      [7, 0, 3],
                      [0],
                      [0, 5],
                      [9],
                      [8]]


def shortest_path(map, start, goal):
    graph = create_graph(map)
    return minimum_cost(graph, start, goal)


def calculate_distance(a, b, intersections):
    point_a = intersections.get(a)
    x_a = point_a[0]
    y_a = point_a[1]
    point_b = intersections.get(b)
    x_b = point_b[0]
    y_b = point_b[1]
    return math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)


def create_graph(map):
    graph = [list() for _ in range(len(map.intersections) + 1)]
    for i in range(0, len(map.roads)):
        for point in map.roads[i]:
            graph[i].append(
                (point, calculate_distance(i, point, map.intersections)))
    return graph


def minimum_cost(graph, start, goal):

    visited = [False for _ in range(len(graph) + 1)]

    min_heap = [(0, start)]

    path = []

    while len(min_heap) > 0:
        cost, current = heapq.heappop(min_heap)

        if visited[current]:
            continue

        for neighbor, edge_cost in graph[current]:
            heapq.heappush(
                min_heap, (edge_cost + calculate_distance(current, goal), neighbor))

        visited[current] = True

    pass


map = M()

shortest_path(map, 0, 5)
