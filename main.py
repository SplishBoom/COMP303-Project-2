from Utilities import safe_start, safe_stop, visualize
from Algorithms import AStar, Dijkstra, MyGraph
import timeit

if __name__ == "__main__" :
    
    safe_start()

    number_of_cities = 100
    start_city = 36
    destination_city = 78

    graph_object = MyGraph(number_of_cities)
    graph_object.generate_graph()
    graph = graph_object.graph

    dijkstra_object = Dijkstra()
    start_of_dijkstra = timeit.default_timer()
    dijkstra_result = dijkstra_object.solve(graph, start_city, destination_city)
    end_of_dijkstra = timeit.default_timer()
    dijkstra_time = (round((end_of_dijkstra - start_of_dijkstra) * 10 ** 6, 3))

    a_star_object = AStar()
    start_of_a_star = timeit.default_timer()
    a_star_result = a_star_object.solve(graph, start_city, destination_city)
    end_of_a_star = timeit.default_timer()
    a_star_time = (round((end_of_a_star - start_of_a_star) * 10 ** 6, 3))

    print("Dijkstra algorithm took " + str(dijkstra_time) + " microseconds.")
    print("Dijkstra algorithm found the shortest path from " + str(start_city) + " to " + str(destination_city) + " with a cost of " + str(dijkstra_result[2]) + " and a distance of " + str(dijkstra_result[3]) + ".")

    print("A* algorithm took " + str(a_star_time) + " microseconds.")
    print("A* algorithm found the shortest path from " + str(start_city) + " to " + str(destination_city) + " with a cost of " + str(a_star_result[2]) + " and a distance of " + str(a_star_result[3]) + ".")

    safe_stop()