from Utilities import safeStart, safeStop, visualize
from Algorithms.MyGraph import MyGraph
from Algorithms.Dijkstra import dijkstra
from Algorithms.AStar import a_star

if __name__ == "__main__" :
    safeStart()
    n = 10
    s = 3
    d = 10

    graph_object = MyGraph(n)
    graph = graph_object.graph

    path_of_node_identities, total_cost, edge_count, number_of_visited_nodes = dijkstra(graph, s, d)
    print(path_of_node_identities, total_cost, edge_count, number_of_visited_nodes)
    #visualize(n, "Djikstra", path_of_node_identities)

    path_of_node_identities, total_cost, edge_count, number_of_visited_nodes = a_star(graph, s, d)
    print(path_of_node_identities, total_cost, edge_count, number_of_visited_nodes)
    #visualize(n, "AStar", path_of_node_identities)

    safeStop()