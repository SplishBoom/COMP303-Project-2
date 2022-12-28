from Utilities import safeStart, safeStop, visualize
from Algorithms.MyGraph import MyGraph
from Algorithms.Dijkstra import dijkstra

if __name__ == "__main__" :
    safeStart()
    n = 15
    s = 7
    d = 2

    graph_object = MyGraph(n)
    graph = graph_object.graph

    path_of_node_identities, total_cost, edge_count = dijkstra(graph, s, d)
    
    visualize(n, "Djikstra", path_of_node_identities)

    safeStop()