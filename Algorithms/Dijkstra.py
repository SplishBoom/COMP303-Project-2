from math import inf
import heapq

"""
Method, that takes an dictionary which includes a directed and weighted graph. Than it finds the shortest path by using Dijkstra's algorithm.
@params:
    graph -> dict : dictionary which includes a directed and weighted graph in the format {node: {neighbour: weight, neighbour: weight, ...}, ...}
    start -> str : start node
    end -> str : end node
@returns:
    path -> list : list of nodes, that are in the shortest path in order
    distance -> int : distance of the shortest path, or number of nodes in the path
    cost -> int : cost of the shortest path, or sum of the weights of the edges in the path
"""
def dijkstra(graph, start, end):

	# initialize distance and cost dictionaries
    total_cost = {node: inf for node in graph}
    edge_count = {node: inf for node in graph}

    # initialize start node
    total_cost[start] = 0
    edge_count[start] = 0

    # initialize priority queue
    queue = [(0, start)]

    # initialize previous node dictionary
    previous = {node: None for node in graph}

    # initialize visited nodes set
    visited = set()

    # loop while queue is not empty
    while queue:

        # pop node with smallest distance from queue
        current_distance, current_node = heapq.heappop(queue)

        # check if node is visited
        if current_node in visited:
            continue

        # add node to visited set
        visited.add(current_node)

        # check if node is end node
        if current_node == end:
            break

        # loop through neighbours
        for neighbour, weight in graph[current_node].items():

            # calculate new distance
            new_distance = current_distance + weight

            # check if new distance is smaller than old distance
            if new_distance < total_cost[neighbour]:

                # update distance and cost dictionaries
                total_cost[neighbour] = new_distance
                edge_count[neighbour] = edge_count[current_node] + 1

                # update previous node dictionary
                previous[neighbour] = current_node

                # push neighbour in queue
                heapq.heappush(queue, (new_distance, neighbour))

    # initialize path list
    path = []

    # initialize current node
    current = end

    # loop while current node is not None
    while current is not None:

        # add current node to path
        path.append(current)

        # update current node
        current = previous[current]

    # reverse path
    path.reverse()

    # return path, distance, cost
    return path, total_cost[end], edge_count[end]